# Generated by Django 3.2.16 on 2022-12-23 23:20

from django.db import migrations
from django.db.models import F


def update_content_locale_array(apps, schema_editor):
    Event = apps.get_model("event", "Event")
    Event.objects.all().update(content_locale_array=F("locale_array"))


class Migration(migrations.Migration):
    dependencies = [
        ("event", "0030_event_content_locale_array"),
    ]

    operations = [
        migrations.RunPython(update_content_locale_array, migrations.RunPython.noop)
    ]