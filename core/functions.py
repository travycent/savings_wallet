from django.core.exceptions import ValidationError
def is_empty(value,name=""):
    if value =="":
        raise ValidationError("{} is a required field".format(str(name)))
    else:
        return value
def is_int(value,name=""):
    if not isinstance(value, int):
        raise ValidationError("{} must be an Integer".format(str(name)))
    else:
        return value
def is_float(value,name=""):
    if not isinstance(value, float):
        raise ValidationError("{} must be an Float".format(str(name)))
    else:
        return value