# Generated by Django 3.2.7 on 2021-09-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=50)),
                ('msg_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
