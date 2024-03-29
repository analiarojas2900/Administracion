# Generated by Django 5.0.1 on 2024-03-14 15:29

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12, validators=[core.validators.validate_rut])),
                ('domicilio', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('afp', models.CharField(choices=[('Provida', 'Provida'), ('Capital', 'Capital'), ('Habitat', 'Habitat'), ('Modelo', 'Modelo'), ('Planvital', 'Planvital')], max_length=20)),
                ('certificado_presentado', models.BooleanField(default=False)),
                ('certificado_presentado_afp', models.FileField(default='', upload_to='certificados_afp/')),
                ('certificado_antecedentes', models.BooleanField(default=False)),
                ('certificado_antecedentes_archivo', models.FileField(default='', upload_to='certificados_antecedentes/')),
                ('copia_carnet', models.BooleanField(default=False)),
                ('copia_carnet_archivo', models.FileField(default='', upload_to='copias_carnet/')),
                ('numero_calzado', models.PositiveSmallIntegerField(choices=[(34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45')], default='34')),
                ('horario', models.CharField(max_length=50)),
                ('sueldo_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.CharField(max_length=20)),
                ('en_caso_emergencia', models.CharField(max_length=20)),
                ('cargo', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_civil', models.CharField(choices=[('Soltero/a', 'Soltero/a'), ('Casado/a', 'Casado/a'), ('Viudo/a', 'Viudo/a'), ('Divorciado/a', 'Divorciado/a'), ('Conviviente', 'Conviviente'), ('Separado/a', 'Separado/a'), ('Union libre', 'Unión libre'), ('Otro', 'Otro')], default='Soltero/a', max_length=20)),
                ('nacimiento', models.CharField(default='', max_length=100)),
                ('nacionalidad', models.CharField(choices=[('Chilena', 'Chilena'), ('Argentina', 'Argentina'), ('Peruana', 'Peruana'), ('Boliviana', 'Boliviana'), ('Colombiana', 'Colombiana'), ('Venezolana', 'Venezolana'), ('Brasileña', 'Brasileña'), ('Ecuatoriana', 'Ecuatoriana'), ('Uruguaya', 'Uruguaya'), ('Paraguaya', 'Paraguaya'), ('Mexicana', 'Mexicana'), ('Estadounidense', 'Estadounidense'), ('Canadiense', 'Canadiense'), ('Española', 'Española'), ('Francesa', 'Francesa')], default='Chilena', max_length=100)),
                ('obra', models.CharField(blank=True, max_length=100, null=True)),
                ('autorizacion', models.CharField(blank=True, max_length=100, null=True)),
                ('salud', models.CharField(choices=[('tramoa', 'TRAMO A'), ('tramob', 'TRAMO B'), ('tramoc', 'TRAMO C'), ('tramod', 'TRAMO D')], default='tramoa', max_length=50)),
                ('certificado_presentado_salud', models.BooleanField(default=False)),
                ('certificado_presentado_salud_archivo', models.FileField(default='', upload_to='certificados_salud/')),
                ('termino_contrato', models.DateField(blank=True, null=True)),
                ('nivel_educacional', models.CharField(choices=[('Educación Básica Completa', 'Educación Básica Completa'), ('Educación Básica Incompleta', 'Educación Básica Incompleta'), ('Educación Media Completa', 'Educación Media Completa'), ('Educación Media Incompleta', 'Educación Media Incompleta'), ('Educación Superior Completa', 'Educación Superior Completa'), ('Educación Superior Incompleta', 'Educación Superior Incompleta')], default='Educación Básica Completa', max_length=100)),
                ('banco', models.CharField(choices=[('Banco de Chile', 'Banco de Chile'), ('Banco Estado', 'Banco Estado'), ('Banco Santander Chile', 'Banco Santander Chile'), ('Banco Itaú Chile', 'Banco Itaú Chile'), ('Banco BCI', 'Banco BCI'), ('Banco Security', 'Banco Security'), ('Banco Falabella', 'Banco Falabella'), ('Banco de Crédito e Inversiones (BCI)', 'Banco de Crédito e Inversiones (BCI)'), ('Scotiabank Chile', 'Scotiabank Chile'), ('Banco BBVA Chile', 'Banco BBVA Chile')], default='Banco de Chile', max_length=100)),
                ('enfermedad', models.BooleanField(default=False)),
                ('cual_enfermedad', models.CharField(blank=True, max_length=100, null=True)),
                ('farmaco', models.BooleanField(default=False)),
                ('cual_farmaco', models.CharField(blank=True, max_length=100, null=True)),
                ('droga', models.BooleanField(default=False)),
            ],
        ),
    ]
