# Generated by Django 4.1.1 on 2023-09-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Img_API', '0015_remove_imgs_pic_imgs_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
