from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput
from django import forms


class ImgsForm(forms.ModelForm):
    class Meta:
        model = Imgs
        fields = ['ID_Type', 'pic', 'new_img','image_url']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'site_name', 'image_url']


# # class ImageForm(forms.ModelForm):
# #     class Meta:
# #         model = Image
# #         fields = ['image', 'site_name', 'image_url']
       
# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Imgs
#         fields = ['ID_Type', 'pic', 'new_img']

#     # تعيين القيمة الافتراضية لحقل new_img إلى '1'
#     new_img = forms.CharField(initial='1')
