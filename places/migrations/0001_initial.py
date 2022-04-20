# Generated by Django 3.2 on 2022-04-20 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, unique=True, verbose_name='адрес')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='широта')),
                ('lot', models.FloatField(blank=True, null=True, verbose_name='долгота')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'место',
                'verbose_name_plural': 'места',
            },
        ),
    ]
