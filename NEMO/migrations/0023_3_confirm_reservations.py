# Generated by Django 2.2.13 on 2020-09-22 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0023_2_confirm_reservations'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='cancellation_reason',
            field=models.TextField(default='', null=True, blank=True, max_length=200, help_text="Shows the reason the reservation was cancelled."),
        ),
    ]