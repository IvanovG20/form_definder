import re


def validate_email(value):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", value))


def validate_phone(value):
    return bool(re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value))


def validate_date(value):
    return (
        bool(re.match(r"^\d{2}\.\d{2}\.\d{4}$", value)) or
        bool(re.match(r"^\d{4}-\d{2}-\d{2}$", value))
    )


def get_field_type(value):
    if validate_date(value):
        return "date"
    if validate_phone(value):
        return "phone"
    if validate_email(value):
        return "email"
    return "text"
