# Generated by Django 3.0.6 on 2020-09-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200928_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=10, verbose_name='name'),
        ),
    ]
