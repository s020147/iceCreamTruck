from django.core.exceptions import ValidationError

def validate_quantity(value):
    if value > flavor.quantity_stocked:
        raise ValidationError("Not enough product in stock")
    return value
