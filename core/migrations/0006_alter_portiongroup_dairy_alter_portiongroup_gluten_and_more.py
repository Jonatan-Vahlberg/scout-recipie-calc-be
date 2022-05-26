# Generated by Django 4.0 on 2022-05-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_portiongroup_xl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portiongroup',
            name='DAIRY',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='GLUTEN',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='LEGUMINOUS',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='MP_ALLERGIES',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='VEGAN',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='VEGITARIAN',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='lg',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='md',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='sm',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='portiongroup',
            name='xs',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
