# Generated by Django 4.0 on 2022-03-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipie', '0006_recipieingredient_replaces_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, choices=[('g', 'g'), ('kg', 'kg'), ('hg', 'hg'), ('ml', 'ml'), ('cl', 'cl'), ('dl', 'dl'), ('l', 'l'), ('st', 'st'), ('tsk', 'tsk'), ('msk', 'msk'), ('krm', 'krm')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='recipieingredient',
            name='replaces_reason',
            field=models.CharField(blank=True, choices=[('VEGITARIAN', 'Vegitarian'), ('VEGAN', 'Vegan'), ('DAIRY', 'Dairy'), ('GLUTEN', 'Gluten'), ('LEGUMINOUS', 'Leguminous'), ('MP_ALLERGIES', 'MIlk protien')], max_length=255, null=True),
        ),
    ]
