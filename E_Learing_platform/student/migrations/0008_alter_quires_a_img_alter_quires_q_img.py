# Generated by Django 5.1 on 2024-11-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_quires_a_img_alter_quires_q_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quires',
            name='a_img',
            field=models.ImageField(blank=True, upload_to='question_model'),
        ),
        migrations.AlterField(
            model_name='quires',
            name='q_img',
            field=models.ImageField(blank=True, upload_to='question_model'),
        ),
    ]
