# Generated by Django 3.1.7 on 2021-03-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]