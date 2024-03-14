from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_rut(value):
    """
    Valida el formato del RUT chileno.
    """
    rut_pattern = r'^\d{1,2}\.\d{3}\.\d{3}-[0-9Kk]$'
    if not re.match(rut_pattern, value):
        raise ValidationError(
            _('El formato del RUT no es válido. Debe ser XX.XXX.XXX-X.'),
            params={'value': value},
        )
    # Verificación del dígito verificador
    value = value.replace('.', '').replace('-', '')
    rut, dv = value[:-1], value[-1]
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    dv_computed = (11 - s % 11) % 11
    dv_computed = 'K' if dv_computed == 10 else str(dv_computed)
    if dv.upper() != dv_computed:
        raise ValidationError(
            _('El RUT no es válido. El dígito verificador es incorrecto.'),
            params={'value': value},
        )
