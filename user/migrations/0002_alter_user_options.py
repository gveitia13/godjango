# Generated by Django 3.2 on 2022-02-10 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('add_product', 'can add product'), ('can_change_product', 'can change product'), ('can_delete_product', 'can delete product'), ('can_view_product', 'can view product')]},
        ),
    ]