# Generated by Django 4.0 on 2021-12-31 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipie', '0003_alter_ingredient_base_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipie',
            old_name='descrtiption',
            new_name='description',
        ),
    ]
