import re

def validate_pin(pin):
    pattern = '[0-9]{6}|[0-9]{4}'
    pin_to_check = re.search(pattern, pin)
    return pin_to_check

validate_pin(111)