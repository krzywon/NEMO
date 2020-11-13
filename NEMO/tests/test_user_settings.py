from django.test import TestCase

from NEMO.models import User, UserPreferences, Account, Project, Area, PhysicalAccessLevel

FAKE_EMAIL_1 = 'test@test.abc'
FAKE_EMAIL_2 = 'test@test.def'
BAD_EMAIL = 'test@nothing'


class ToolTestCase(TestCase):
    area: Area = None
    area_access_level = None
    consumer: User = None
    staff: User = None
    superuser: User = None
    project: Project = None

    def setUp(self):
        global area, area_access_level, owner, consumer, staff, superuser, project
        account = Account.objects.create(name="account1")
        project = Project.objects.create(name="project1", account=account)
        area = Area.objects.create(name='test_area', requires_reservation=True, category='Imaging')
        area_access_level = PhysicalAccessLevel.objects.create(name='area access level', area=area,
                                                               schedule=PhysicalAccessLevel.Schedule.ALWAYS)
        staff = User.objects.create(username='staff', first_name='Staff', last_name='Member', is_staff=True)
        superuser = User.objects.create(username='superuser', first_name='Superuser', last_name='Member',
                                        is_superuser=True)
        consumer = User.objects.create(username='jsmith', first_name='John', last_name='Smith', training_required=False)
        consumer.physical_access_levels.add(area_access_level)
        consumer.projects.add(project)
        consumer.save()
        consumer.preferences = UserPreferences()

    def test_base_settings(self):
        self.assertEqual(consumer.get_full_name(), 'John Smith (jsmith)')
        self.assertEqual(consumer.get_name(), 'John Smith')
        self.assertEqual(consumer.get_short_name(), 'John')
        self.assertEqual(consumer.supervisor.count(), 0)
        self.assertFalse(consumer.training_required)
        self.assertFalse(consumer.is_staff)
        self.assertFalse(consumer.is_superuser)
        self.assertFalse(consumer.is_technician)
        self.assertFalse(consumer.is_service_personnel)
        self.assertTrue(consumer.is_active)

        preferences = consumer.get_preferences()
        self.assertFalse(preferences.alternate_email_address)
        self.assertFalse(preferences.attach_created_reservation)
        self.assertFalse(preferences.attach_cancelled_reservation)
        self.assertFalse(preferences.attach_confirmed_reservation)

    def test_change_email(self):
        consumer.email = FAKE_EMAIL_1
        self.assertEqual(len(consumer.get_email_list()), 1)

        # Test using same email addresses in User and in alternate
        consumer.preferences.alternate_email_address = FAKE_EMAIL_1
        emails = consumer.get_email_list()
        self.assertEqual(len(emails), 2)
        self.assertEqual(emails[0], emails[1])

        # Test different email addresses in User and in alternate
        consumer.preferences.alternate_email_address = FAKE_EMAIL_2
        emails = consumer.get_email_list()
        self.assertEqual(len(emails), 2)
        self.assertNotEqual(emails[0], emails[1])

    def test_set_supervisors(self):
        staff.email = FAKE_EMAIL_1
        staff.save()
        staff.preferences = UserPreferences()
        self.assertEqual(consumer.supervisor.count(), 0)
        self.assertEqual(len(consumer.supervisor_email_list()), 0)
        consumer.supervisor.add(superuser)
        self.assertEqual(consumer.supervisor.count(), 1)
        self.assertEqual(len(consumer.supervisor_email_list()), 1)
        self.assertNotIn(FAKE_EMAIL_1, consumer.supervisor_email_list())
        consumer.supervisor.add(staff)
        self.assertEqual(consumer.supervisor.count(), 2)
        self.assertEqual(len(consumer.supervisor_email_list()), 2)
        self.assertIn(FAKE_EMAIL_1, consumer.supervisor_email_list())
        consumer.supervisor.remove(superuser)
        self.assertEqual(consumer.supervisor.count(), 1)
        self.assertEqual(len(consumer.supervisor_email_list()), 1)
        consumer.supervisor.remove(staff)
        self.assertEqual(consumer.supervisor.count(), 0)
        self.assertEqual(len(consumer.supervisor_email_list()), 0)

    def test_set_invalid_user_values(self):
        # TODO: Write more here...
        self.assertEqual(consumer.supervisor.count(), 0)
        self.assertRaises(ValueError, consumer.supervisor.add, FAKE_EMAIL_1)
