# Generated by Django 5.1 on 2024-10-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_rename_theme1_free_course_theme_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='link1',
            field=models.FileField(default='null', upload_to='recorded_lectures'),
        ),
        migrations.AlterField(
            model_name='course',
            name='link2',
            field=models.FileField(default='null', upload_to='recorded_lectures'),
        ),
        migrations.AlterField(
            model_name='course',
            name='link3',
            field=models.FileField(default='null', upload_to='recorded_lectures'),
        ),
        migrations.AlterField(
            model_name='course',
            name='link4',
            field=models.FileField(default='null', upload_to='recorded_lectures'),
        ),
        migrations.AlterField(
            model_name='course',
            name='link5',
            field=models.FileField(default='null', upload_to='recorded_lectures'),
        ),
    ]
