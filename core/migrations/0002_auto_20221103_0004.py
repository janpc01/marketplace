# Generated by Django 2.2.13 on 2022-11-03 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('R', 'Regular'), ('J', 'Jumbo'), ('S', 'Special')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('R', 'Regular'), ('J', 'Jumbo'), ('S', 'Special')], default='P', max_length=1),
            preserve_default=False,
        ),
    ]
