from django.db import models
from .validators import validate_rut

def image_upload_path(instance, filename):
    return f'core/static/img/empleados/{instance.id}/{filename}'

class Empleado(models.Model):
    fecha_ingreso = models.DateField(null=True, blank=True)
    nombre_completo = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, validators=[validate_rut])
    domicilio = models.TextField()
    correo = models.EmailField()
    afp = models.CharField(max_length=20, choices=(
        ("Provida", "Provida"),
        ("Capital", "Capital"),
        ("Habitat", "Habitat"),
        ("Modelo", "Modelo"),
        ("Planvital", "Planvital"),
    ))
    certificado_presentado = models.BooleanField(default=False)
    certificado_presentado_afp = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    certificado_antecedentes = models.BooleanField(default=False)
    certificado_antecedentes_archivo = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    copia_carnet = models.BooleanField(default=False)
    copia_carnet_archivo = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    numero_calzado = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(34, 46)], default=34)
    horario = models.CharField(max_length=255)
    sueldo_base = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    en_caso_emergencia = models.CharField(max_length=20)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, choices=(
        ("Soltero/a", "Soltero/a"), ("Casado/a", "Casado/a"), ("Viudo/a", "Viudo/a"),
        ("Divorciado/a", "Divorciado/a"), ("Conviviente", "Conviviente"),
        ("Separado/a", "Separado/a"), ("Unión libre", "Unión libre"), ("Otro", "Otro"),
    ), default="Soltero/a")
    nacimiento = models.CharField(max_length=100, default="")
    nacionalidad = models.CharField(max_length=100, choices=(
        ("Chilena", "Chilena"), ("Argentina", "Argentina"), ("Peruana", "Peruana"),
        ("Boliviana", "Boliviana"), ("Colombiana", "Colombiana"), ("Venezolana", "Venezolana"),
        ("Brasileña", "Brasileña"), ("Ecuatoriana", "Ecuatoriana"), ("Uruguaya", "Uruguaya"),
        ("Paraguaya", "Paraguaya"), ("Mexicana", "Mexicana"), ("Estadounidense", "Estadounidense"),
        ("Canadiense", "Canadiense"), ("Española", "Española"), ("Francesa", "Francesa"),
    ))
    obra = models.CharField(max_length=100, blank=True, null=True)
    autorizacion = models.CharField(max_length=100, blank=True, null=True)
    salud = models.CharField(max_length=50, choices=(
        ("tramoa", "TRAMO A"), ("tramob", "TRAMO B"), ("tramoc", "TRAMO C"), ("tramod", "TRAMO D"),
    ))
    certificado_presentado_salud = models.BooleanField(default=False)
    certificado_presentado_salud_archivo = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
    termino_contrato = models.DateField(null=True, blank=True)
    nivel_educacional = models.CharField(max_length=100, choices=(
        ("Educación Básica Completa", "Educación Básica Completa"),
        ("Educación Básica Incompleta", "Educación Básica Incompleta"),
        ("Educación Media Completa", "Educación Media Completa"),
        ("Educación Media Incompleta", "Educación Media Incompleta"),
        ("Educación Superior Completa", "Educación Superior Completa"),
        ("Educación Superior Incompleta", "Educación Superior Incompleta"),
    ))
    banco = models.CharField(max_length=100, choices=[
        ("Banco de Chile", "Banco de Chile"), ("Banco Estado", "Banco Estado"),
        ("Banco Santander Chile", "Banco Santander Chile"), ("Banco Itaú Chile", "Banco Itaú Chile"),
        ("Banco BCI", "Banco BCI"), ("Banco Security", "Banco Security"),
        ("Banco Falabella", "Banco Falabella"),
        ("Banco de Crédito e Inversiones (BCI)", "Banco de Crédito e Inversiones (BCI)"),
        ("Scotiabank Chile", "Scotiabank Chile"), ("Banco BBVA Chile", "Banco BBVA Chile"),
    ])
    enfermedad = models.BooleanField(default=False)
    cual_enfermedad = models.CharField(max_length=100, blank=True, null=True)
    farmaco = models.BooleanField(default=False)
    cual_farmaco = models.CharField(max_length=100, blank=True, null=True)
    droga = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.certificado_presentado_salud:
            self.certificado_presentado_salud_archivo = None
        if not self.certificado_antecedentes:
            self.certificado_antecedentes_archivo = None
        if not self.certificado_presentado_afp:
            self.certificado_presentado_afp = None
        if not self.copia_carnet:
            self.copia_carnet_archivo = None
        if not self.enfermedad:
            self.cual_enfermedad = None  
        if not self.farmaco:
            self.cual_farmaco = None  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_completo
