# Generated by Django 2.2.4 on 2020-08-02 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0005_auto_20200802_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='Referencia',
            field=models.CharField(max_length=60, null=True, verbose_name='Referencias'),
        ),
    ]
