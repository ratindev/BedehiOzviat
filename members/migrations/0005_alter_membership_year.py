# Generated by Django 4.2 on 2024-02-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_kardan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='year',
            field=models.IntegerField(verbose_name='سالهای عضویت'),
        ),
    ]