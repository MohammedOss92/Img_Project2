# Generated by Django 4.1.1 on 2023-09-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Img_API', '0016_alter_imagefile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgs',
            name='pic',
        ),
        migrations.DeleteModel(
            name='ImageFile',
        ),
        migrations.AddField(
            model_name='imgs',
            name='pic',
            field=models.ImageField(default='10:5', upload_to=''),
            preserve_default=False,
        ),
    ]
