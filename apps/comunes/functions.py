from django.contrib.contenttypes.models import ContentType

# How to use
# obj = [User].objects.create()
# get_app_name(obj)
# get_model_name(obj)

# __package__.split('.')[1]
# self._meta.verbose_name.lower()

def get_app_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.app_label

def get_model_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.model
