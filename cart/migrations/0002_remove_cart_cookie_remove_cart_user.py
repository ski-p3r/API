# Generated by Django 4.2.5 on 2023-09-28 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cookie',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]