# Generated by Django 5.0.6 on 2024-07-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categroy',
            field=models.BooleanField(default=False),
        ),
    ]
