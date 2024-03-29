# Generated by Django 4.1.1 on 2023-09-05 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Img_API', '0008_delete_imgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images/')),
                ('new_img', models.CharField(default=1, max_length=2, null=True)),
                ('site_name', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('ID_Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Img_API.img_type')),
            ],
        ),
    ]
