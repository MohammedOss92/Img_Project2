# Generated by Django 4.1.1 on 2023-09-05 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Img_API', '0006_rename_pic_url_imgs_image_url_imgs_site_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]