# Generated by Django 4.2.11 on 2025-03-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='categories/', verbose_name='Imagine fon'),
        ),
    ]
