# Generated by Django 5.1 on 2024-10-30 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_alter_course_link1_alter_course_link2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='link1',
        ),
        migrations.RemoveField(
            model_name='course',
            name='link2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='link3',
        ),
        migrations.RemoveField(
            model_name='course',
            name='link4',
        ),
        migrations.RemoveField(
            model_name='course',
            name='link5',
        ),
    ]
