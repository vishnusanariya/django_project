# Generated by Django 4.0 on 2022-02-26 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_history_job_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='deal',
            fields=[
                ('deal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jobs.jobs')),
                ('status', models.BooleanField(default=False)),
                ('job_title', models.CharField(default='nuoln', max_length=30)),
                ('job_worker', models.CharField(max_length=30)),
                ('job_creater_approval', models.BooleanField(default=False)),
            ],
        ),
    ]
