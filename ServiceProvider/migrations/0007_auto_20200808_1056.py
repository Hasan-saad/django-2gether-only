# Generated by Django 3.0.8 on 2020-08-08 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceProvider', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='servicProvider',
            new_name='serviceProvider',
        ),
    ]
