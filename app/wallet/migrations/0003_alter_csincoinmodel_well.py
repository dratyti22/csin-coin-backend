# Generated by Django 4.2.15 on 2024-09-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_csincoinmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csincoinmodel',
            name='well',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Курс'),
        ),
    ]
