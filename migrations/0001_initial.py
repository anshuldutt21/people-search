# Generated by Django 3.0.3 on 2020-09-27 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_STUDENT_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_email_id', models.CharField(choices=[('all', 'All'), ('students', 'All Students'), ('faculty', 'All Faculty')], default='all', max_length=20)),
                ('primary_mobile_no', models.CharField(choices=[('all', 'All'), ('students', 'All Students'), ('faculty', 'All Faculty')], default='all', max_length=20)),
                ('room_no', models.CharField(choices=[('all', 'All'), ('students', 'All Students'), ('faculty', 'All Faculty')], default='all', max_length=20)),
                ('bhawan', models.CharField(choices=[('all', 'All'), ('students', 'All Students'), ('faculty', 'All Faculty')], default='all', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
        ),
    ]
