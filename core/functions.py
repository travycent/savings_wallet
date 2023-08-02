from django.core.exceptions import ValidationError
from dateutil import parser
from datetime import date,datetime
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
def is_date(value,name=""):
    try:
        parser.parse(value)
        return value
    except ValueError:
        raise ValidationError("{} : Invalid date format. Please provide a valid date.".format(str(name)))
def is_date_greater(from_date,to_date):
    from_date=datetime.strptime(from_date, "%Y-%m-%d").date()
    to_date=datetime.strptime(to_date, "%Y-%m-%d").date()
    if from_date >= date.today() and to_date >= from_date:
        return True
    else:
        raise ValidationError("Both Dates should be greater than today's Date")
            
