from django.views.generic import View


def is_sublclass(klass, super_class):

    try:
        return issubclass(klass, super_class) and not klass is super_class
    except:
        return False


def is_valid_view(value, root_module):

    return is_sublclass(value, View) and hasattr(value, "__module__") and root_module in value.__module__
