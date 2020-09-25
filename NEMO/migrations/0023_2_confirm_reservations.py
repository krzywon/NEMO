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
            name='cancellation_reason',
            field=models.BooleanField(default=True, help_text='When checked, the reservation has been confirmed by an admin of the area/tool/etc.'),
        ),
    ]