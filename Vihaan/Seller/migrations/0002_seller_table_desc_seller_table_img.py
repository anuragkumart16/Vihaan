# Generated by Django 4.1.1 on 2022-10-26 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller_table',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='seller_table',
            name='img',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
