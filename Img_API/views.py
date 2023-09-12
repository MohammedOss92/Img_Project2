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
    uploaded_image_url = None  # ابدأ بتعيينها إلى None

    if request.method == 'POST':
        form = ImgsForm(request.POST, request.FILES)
        if form.is_valid():
            img_instance = form.save()
            # إذا تم رفع الصورة بنجاح، استخدم request.build_absolute_uri لإنشاء الرابط المطلق
            uploaded_image_url = request.build_absolute_uri(img_instance.pic.url)
            # يمكنك أيضًا تمرير أي بيانات إضافية تحتاجها إلى القالب هنا
            img_instance.image_url = uploaded_image_url  # إضافة الرابط المطلق إلى الكائن img_instance
            img_instance.save()
    else:
        form = ImgsForm()

    return render(request, 'aa/img.html', {'form': form, 'uploaded_image_url': uploaded_image_url})

##########################################################
def add_imgs(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            # �� ������ ���� ������ ������ ����� �� ��� "image_url"
            image.image_url = request.build_absolute_uri(image.image.url)

            image.save()
            return redirect('home')  # �� ������ �������� ��� ���� ����� ����� ��� ����� �����
    else:
        form = ImageForm()
    return render(request, 'aa/a.html', {'form': form})

