# Generated by Django 4.0 on 2021-12-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipie', '0002_alter_ingredient_category_alter_ingredient_recipie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='base_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
