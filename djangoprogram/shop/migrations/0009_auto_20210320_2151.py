# Generated by Django 3.1.7 on 2021-03-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='item_json',
            new_name='items_json',
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=111),
        ),
    ]
