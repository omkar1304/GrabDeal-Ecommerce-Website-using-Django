# Generated by Django 4.0.4 on 2022-04-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
