# Generated by Django 4.2.5 on 2023-09-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100, null=True)),
                ('new_image', models.CharField(default=1, max_length=2)),
            ],
        ),
    ]
