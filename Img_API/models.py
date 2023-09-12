from django.db import models

# Create your models here.
class Img_Type(models.Model):
    Category = models.CharField(max_length=100, null=True)
    new_image = models.CharField(max_length=2,default=1)

    def __str__(self):
        return self.Category
    
class Imgs(models.Model):
     ID_Type = models.ForeignKey(Img_Type, null=True, on_delete=models.SET_NULL)
     pic = models.ImageField(upload_to='')
     new_img = models.CharField(max_length=2, null=True,default=1)
     image_url = models.URLField(null=True, blank=True)


class Image(models.Model):
    image = models.ImageField(upload_to='')
    site_name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
