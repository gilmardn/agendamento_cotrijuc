# Generated by Django 5.0.4 on 2024-04-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filial',
            name='numero',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='saldo',
            name='tergrasa',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='saldo',
            name='termasa',
            field=models.IntegerField(default=0),
        ),
    ]
