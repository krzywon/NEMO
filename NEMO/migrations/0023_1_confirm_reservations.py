# Generated by Django 2.2.13 on 2020-09-22 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0023_badgereader'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='confirmed',
            field=models.BooleanField(default=True, help_text='When checked, the reservation has been confirmed by an admin of the area/tool/etc.'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='confirmed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservation_confirmer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='confirmed_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userpreferences',
            name='attach_confirmed_reservation',
            field=models.BooleanField('confirmed_reservation_invite', default=False, help_text='Whether or not to send a calendar invitation when a reservation is confirmed'),
        )
    ]