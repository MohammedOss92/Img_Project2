# Generated by Django 4.1.1 on 2023-09-11 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Img_API', '0013_remove_imgs_site_name_alter_imgs_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
