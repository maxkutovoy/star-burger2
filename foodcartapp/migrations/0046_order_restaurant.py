# Generated by Django 3.2 on 2022-04-18 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0045_auto_20220417_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='foodcartapp.restaurant', verbose_name='ресторан доставки'),
            preserve_default=False,
        ),
    ]
