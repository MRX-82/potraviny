# Generated by Django 4.2.1 on 2023-11-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='D', max_length=50),
        ),
    ]
