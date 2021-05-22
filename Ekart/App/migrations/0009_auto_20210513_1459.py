# Generated by Django 3.0 on 2021-05-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='Doorno',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='city',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='state',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='streetname',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]