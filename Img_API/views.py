from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
from django.conf import settings
from .utils import is_valid_data  # استبدال mymodule بالمكتبة أو الملف الصحيح





def index(request):
    context = {
    }
    return render(request,"aa/index.html",context)


def create_img_type(request):
    message = ""  # سيتم تخزين الرسالة هنا

    if request.method == 'POST':
        img_type_name = request.POST.get('img_type_name')
        new_image_value = request.POST.get('new_image', '1')  # استخراج القيمة من النموذج

        # إنشاء سجل جديد في نموذج Img_Type مع اسم الفئة وقيمة new_image
        if img_type_name:
            img_type, created = Img_Type.objects.get_or_create(Category=img_type_name, defaults={'new_image': new_image_value})
            message = "تم" if created else "الفئة موجودة بالفعل"  # تعيين الرسالة إلى "تم" أو "الفئة موجودة بالفعل" بناءً على ما إذا كان تم إنشاء السجل

    return render(request, 'aa/add.html', {'message': message})


def add_img_withTypeType(request):
    uploaded_image_urls = []

    if request.method == 'POST':
        form = ImgsForm(request.POST, request.FILES)
        if form.is_valid():
            # حصل على قائمة الصور المرسلة
            images = request.FILES.getlist('pic')

            for image_file in images:
                # قم بحفظ كل صورة في نموذج Imgs منفردة
                img_instance = Imgs(pic=image_file)
                
                # قم بتعيين القيمة لحقل ID_Type من النموذج Img_Type المحدد في النموذج
                img_instance.ID_Type = form.cleaned_data['ID_Type']
                
                img_instance.save()

                # إذا تم رفع الصورة بنجاح، استخدم request.build_absolute_uri لإنشاء الرابط المطلق
                uploaded_image_url = request.build_absolute_uri(img_instance.pic.url)
                
                # حفظ الرابط في حقل image_url في نموذج Imgs
                img_instance.image_url = uploaded_image_url
                img_instance.save()

                uploaded_image_urls.append(uploaded_image_url)

    else:
        form = ImgsForm()

    return render(request, 'aa/img.html', {'form': form, 'uploaded_image_urls': uploaded_image_urls})



# def add_img_withTypeType(request):
#     uploaded_image_urls = []

#     if request.method == 'POST':
#         form = ImgsForm(request.POST, request.FILES)
#         if form.is_valid():
#             # حصل على قائمة الصور المرسلة
#             images = request.FILES.getlist('pic')

#             for image_file in images:
#                 # قم بحفظ كل صورة في نموذج Imgs منفردة
#                 img_instance = Imgs(pic=image_file)
                
#                 # قم بتعيين القيمة لحقل ID_Type من النموذج Img_Type المحدد في النموذج
#                 img_instance.ID_Type = form.cleaned_data['ID_Type']
                
#                 img_instance.save()

#                 # إذا تم رفع الصورة بنجاح، استخدم request.build_absolute_uri لإنشاء الرابط المطلق
#                 uploaded_image_url = request.build_absolute_uri(img_instance.pic.url)
#                 uploaded_image_urls.append(uploaded_image_url)
#                 img_instance.save()

#     else:
#         form = ImgsForm()

#     return render(request, 'aa/img.html', {'form': form, 'uploaded_image_urls': uploaded_image_urls})

##########################################################
def add_imgs(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image')


            for image_file in images:
                image_instance = Image(image=image_file)
                image_instance.save()

                uploaded_image_url = request.build_absolute_uri(image_instance.image.url)
                image_instance.image_url = uploaded_image_url
                image_instance.save()

            # image = form.save(commit=False)
            # # �� ������ ���� ������ ������ ����� �� ��� "image_url"
            # image.image_url = request.build_absolute_uri(image.image.url)

            # image.save()
            # return redirect('home')  # �� ������ �������� ��� ���� ����� ����� ��� ����� �����
    else:
        form = ImageForm()
    return render(request, 'aa/a.html', {'form': form})

def add_photos(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # قائمة الملفات المرسلة من النموذج
            images = request.FILES.getlist('image')

            # حفظ كل ملف في قاعدة البيانات
            for image_file in images:
                image_instance = Image(image=image_file)
                image_instance.save()

                uploaded_image_url = request.build_absolute_uri(image_instance.image.url)
                image_instance.image_url = uploaded_image_url
                image_instance.save()

            # return redirect('gallery')
    else:
        form = PhotoForm()
    
    return render(request, 'aa/s.html', {'form': form})
