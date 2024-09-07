# Generated by Django 4.2.15 on 2024-09-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsinCoinModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turnover', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Оборот')),
                ('number_coins', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Количество монет')),
                ('well', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Курс')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Курс CsinCoin',
                'verbose_name_plural': 'Курсы CsinCoin',
                'db_table': 'csin_coin_model',
            },
        ),
    ]
