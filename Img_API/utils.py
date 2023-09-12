
def is_valid_data(img_type_name, new_image_value):
    # قم بتنفيذ الاختبارات الخاصة بك هنا للتحقق مما إذا كانت البيانات صالحة أم لا
    # على سبيل المثال:
    if len(img_type_name) > 0 and new_image_value.isdigit():
        return True
    else:
        return False