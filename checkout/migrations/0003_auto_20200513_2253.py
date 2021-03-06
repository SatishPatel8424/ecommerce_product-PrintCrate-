# Generated by Django 3.0.5 on 2020-05-13 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200511_1234'),
        ('checkout', '0002_auto_20200513_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='total',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
