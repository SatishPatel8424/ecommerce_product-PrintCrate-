# Generated by Django 3.0.5 on 2020-05-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200526_0943'),
        ('checkout', '0015_auto_20200526_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
    ]