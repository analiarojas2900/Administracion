from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['fecha_ingreso', 'nombre_completo', 'rut', 'domicilio', 'correo', 'afp', 'certificado_presentado', 'certificado_presentado_afp', 'certificado_antecedentes', 'certificado_antecedentes_archivo', 'copia_carnet', 'copia_carnet_archivo', 'numero_calzado', 'horario', 'sueldo_base', 'telefono', 'en_caso_emergencia', 'cargo', 'estado_civil', 'nacimiento', 'nacionalidad', 'obra', 'autorizacion', 'salud', 'certificado_presentado_salud', 'certificado_presentado_salud_archivo', 'termino_contrato', 'nivel_educacional', 'banco', 'enfermedad', 'cual_enfermedad', 'farmaco', 'cual_farmaco', 'droga']
