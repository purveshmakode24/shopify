# Generated by Django 2.2.2 on 2019-07-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='products/%Y/%m/%d'),
        ),
    ]
