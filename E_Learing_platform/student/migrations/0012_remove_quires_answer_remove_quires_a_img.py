# Generated by Django 5.1 on 2024-11-15 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_alter_quires_a_img_alter_quires_q_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quires',
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='quires',
            name='a_img',
        ),
    ]