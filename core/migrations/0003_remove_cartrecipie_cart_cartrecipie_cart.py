# Generated by Django 4.0 on 2022-05-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_portiongroup_dairy_alter_portiongroup_gluten_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartrecipie',
            name='cart',
        ),
        migrations.AddField(
            model_name='cartrecipie',
            name='cart',
            field=models.ManyToManyField(to='core.Cart'),
        ),
    ]