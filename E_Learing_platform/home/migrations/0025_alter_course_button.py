# Generated by Django 5.1 on 2024-09-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='button',
            field=models.CharField(default='/log', max_length=100),
        ),
    ]