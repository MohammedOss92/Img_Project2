# Generated by Django 4.1.1 on 2023-09-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Img_API', '0012_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgs',
            name='site_name',
        ),
        migrations.AlterField(
            model_name='imgs',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
