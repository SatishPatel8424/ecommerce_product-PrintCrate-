# Generated by Django 3.0.5 on 2020-04-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200418_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='showcase_product',
            field=models.BooleanField(default=False),
        ),
    ]