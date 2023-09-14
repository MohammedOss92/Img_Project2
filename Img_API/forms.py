from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput
from django import forms


# class ImgsForm(forms.ModelForm):
#     class Meta:
#         model = Imgs
#         fields = ['ID_Type', 'pic', 'new_img', 'image_url']
#     pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class ImgsForm(forms.ModelForm):
    ID_Type = forms.ModelChoiceField(queryset=Img_Type.objects.all(), required=False)
    
    class Meta:
        model = Imgs
        fields = ['ID_Type', 'pic', 'new_img', 'image_url']
    pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
   

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'site_name', 'image_url']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'site_name', 'image_url']
        # fields = ['description', 'image']


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
