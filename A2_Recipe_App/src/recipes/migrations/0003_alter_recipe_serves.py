# Generated by Django 4.2.14 on 2024-08-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_cooking_time_alter_recipe_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.PositiveIntegerField(),
        ),
    ]
