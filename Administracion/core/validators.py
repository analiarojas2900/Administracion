from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_rut(rut):
    rut = rut.replace('.', '').replace('-', '')  # Remove dots and dashes
    if len(rut) != 9:
        raise ValidationError("El RUT debe tener 9 dígitos.")
    try:
        int(rut[:-1])
    except ValueError:
        raise ValidationError("Los primeros 8 dígitos del RUT deben ser numéricos.")
    multipliers = [2, 3, 4, 5, 6, 7, 2, 3]
    total = sum(int(digit) * multiplier for digit, multiplier in zip(reversed(rut[:-1]), multipliers))
    verifier = 11 - (total % 11)
    verifier = str(verifier) if verifier != 10 else 'K'
    if verifier != rut[-1].upper():
        raise ValidationError("El dígito verificador del RUT es incorrecto.")
