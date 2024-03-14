from django.db import models, migrations
from .validators import validate_rut
from django.utils import timezone

def image_upload_path(instance, filename):
    return f'core/static/img/empleados/{instance.id}/{filename}'

class Empleado(models.Model):
    fecha_ingreso = models.DateField(null=True, blank=True)
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, validators=[validate_rut])
    domicilio = models.CharField(max_length=255)
    correo = models.EmailField()
    afp = models.CharField(max_length=20, choices=(
        ("Provida", "Provida"),
        ("Capital", "Capital"),
        ("Habitat", "Habitat"),
        ("Modelo", "Modelo"),
        ("Planvital", "Planvital"),
    ))
    certificado_presentado = models.BooleanField(default=False)
    certificado_presentado_afp = models.FileField(upload_to='certificados_afp/', default="")
    certificado_antecedentes = models.BooleanField(default=False)
    certificado_antecedentes_archivo = models.FileField(upload_to='certificados_antecedentes/', default="")
    copia_carnet = models.BooleanField(default=False)
    copia_carnet_archivo = models.FileField(upload_to='copias_carnet/', default="")
    numero_calzado = models.PositiveSmallIntegerField(choices=[
        (34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'),
        (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45'),
    ], default="34")
    horario = models.CharField(max_length=50)
    sueldo_base = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    en_caso_emergencia = models.CharField(max_length=20)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, choices=(
        ("Soltero/a", "Soltero/a"), ("Casado/a", "Casado/a"), ("Viudo/a", "Viudo/a"),
        ("Divorciado/a", "Divorciado/a"), ("Conviviente", "Conviviente"),
        ("Separado/a", "Separado/a"), ("Union libre", "Unión libre"), ("Otro", "Otro"),
    ), default="Soltero/a")
    nacimiento = models.CharField(max_length=100, default="")
    nacionalidad = models.CharField(max_length=100, choices=(
        ("Chilena", "Chilena"), ("Argentina", "Argentina"), ("Peruana", "Peruana"),
        ("Boliviana", "Boliviana"), ("Colombiana", "Colombiana"), ("Venezolana", "Venezolana"),
        ("Brasileña", "Brasileña"), ("Ecuatoriana", "Ecuatoriana"), ("Uruguaya", "Uruguaya"),
        ("Paraguaya", "Paraguaya"), ("Mexicana", "Mexicana"), ("Estadounidense", "Estadounidense"),
        ("Canadiense", "Canadiense"), ("Española", "Española"), ("Francesa", "Francesa"),
    ), default="Chilena")
    obra = models.CharField(max_length=100, blank=True, null=True)
    autorizacion = models.CharField(max_length=100, blank=True, null=True)
    salud = models.CharField(max_length=50, choices=(
        ("tramoa", "TRAMO A"), ("tramob", "TRAMO B"), ("tramoc", "TRAMO C"), ("tramod", "TRAMO D"),
    ), default="tramoa")
    certificado_presentado_salud = models.BooleanField(default=False)
    certificado_presentado_salud_archivo = models.FileField(upload_to='certificados_salud/', default="")
    termino_contrato = models.DateField(null=True, blank=True)
    nivel_educacional = models.CharField(max_length=100, choices=(
        ("Educación Básica Completa", "Educación Básica Completa"),
        ("Educación Básica Incompleta", "Educación Básica Incompleta"),
        ("Educación Media Completa", "Educación Media Completa"),
        ("Educación Media Incompleta", "Educación Media Incompleta"),
        ("Educación Superior Completa", "Educación Superior Completa"),
        ("Educación Superior Incompleta", "Educación Superior Incompleta"),
    ), default="Educación Básica Completa")
    banco = models.CharField(max_length=100, choices=(
        ("Banco de Chile", "Banco de Chile"), ("Banco Estado", "Banco Estado"),
        ("Banco Santander Chile", "Banco Santander Chile"), ("Banco Itaú Chile", "Banco Itaú Chile"),
        ("Banco BCI", "Banco BCI"), ("Banco Security", "Banco Security"),
        ("Banco Falabella", "Banco Falabella"),
        ("Banco de Crédito e Inversiones (BCI)", "Banco de Crédito e Inversiones (BCI)"),
        ("Scotiabank Chile", "Scotiabank Chile"), ("Banco BBVA Chile", "Banco BBVA Chile"),
    ), default="Banco de Chile")
    enfermedad = models.BooleanField(default=False)
    cual_enfermedad = models.CharField(max_length=100, blank=True, null=True)
    farmaco = models.BooleanField(default=False)
    cual_farmaco = models.CharField(max_length=100, blank=True, null=True)
    droga = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_completo
