# Generated by Django 4.2.8 on 2023-12-20 20:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fortune", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Question",
            new_name="Quote",
        ),
    ]
