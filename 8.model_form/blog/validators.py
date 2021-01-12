from django.core.exceptions import ValidationError


def validate_author(value):
    judul_input = value
    if judul_input == "Lukman":
        massage = judul_input +" tidak bisa diposting"
        raise ValidationError(massage)