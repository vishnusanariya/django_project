# Generated by Django 4.0 on 2022-02-04 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginmodule', '0010_alter_regis_uname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='_regis',
            new_name='regis',
        ),
    ]
