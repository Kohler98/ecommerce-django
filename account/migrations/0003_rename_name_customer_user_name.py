# Generated by Django 4.2.7 on 2023-12-11 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customer_address_delete_userbase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='user_name',
        ),
    ]