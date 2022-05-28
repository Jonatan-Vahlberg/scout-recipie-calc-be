# Generated by Django 4.0 on 2022-05-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipie', '0007_alter_ingredient_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipie',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipies', through='recipie.RecipieIngredient', to='recipie.Ingredient'),
        ),
    ]
