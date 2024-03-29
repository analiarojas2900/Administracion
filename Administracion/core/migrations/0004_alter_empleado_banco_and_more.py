# Generated by Django 5.0.1 on 2024-03-20 14:47

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_empleado_certificado_antecedentes_archivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='banco',
            field=models.CharField(choices=[('Banco de Chile', 'Banco de Chile'), ('Banco Estado', 'Banco Estado'), ('Banco Santander Chile', 'Banco Santander Chile'), ('Banco Itaú Chile', 'Banco Itaú Chile'), ('Banco BCI', 'Banco BCI'), ('Banco Security', 'Banco Security'), ('Banco Falabella', 'Banco Falabella'), ('Banco de Crédito e Inversiones (BCI)', 'Banco de Crédito e Inversiones (BCI)'), ('Scotiabank Chile', 'Scotiabank Chile'), ('Banco BBVA Chile', 'Banco BBVA Chile')], max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='certificado_antecedentes_archivo',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.image_upload_path),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='certificado_presentado_afp',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.image_upload_path),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='certificado_presentado_salud_archivo',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.image_upload_path),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='copia_carnet_archivo',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.image_upload_path),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='domicilio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='estado_civil',
            field=models.CharField(choices=[('Soltero/a', 'Soltero/a'), ('Casado/a', 'Casado/a'), ('Viudo/a', 'Viudo/a'), ('Divorciado/a', 'Divorciado/a'), ('Conviviente', 'Conviviente'), ('Separado/a', 'Separado/a'), ('Unión libre', 'Unión libre'), ('Otro', 'Otro')], default='Soltero/a', max_length=20),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='horario',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nacionalidad',
            field=models.CharField(choices=[('Chilena', 'Chilena'), ('Argentina', 'Argentina'), ('Peruana', 'Peruana'), ('Boliviana', 'Boliviana'), ('Colombiana', 'Colombiana'), ('Venezolana', 'Venezolana'), ('Brasileña', 'Brasileña'), ('Ecuatoriana', 'Ecuatoriana'), ('Uruguaya', 'Uruguaya'), ('Paraguaya', 'Paraguaya'), ('Mexicana', 'Mexicana'), ('Estadounidense', 'Estadounidense'), ('Canadiense', 'Canadiense'), ('Española', 'Española'), ('Francesa', 'Francesa')], max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nivel_educacional',
            field=models.CharField(choices=[('Educación Básica Completa', 'Educación Básica Completa'), ('Educación Básica Incompleta', 'Educación Básica Incompleta'), ('Educación Media Completa', 'Educación Media Completa'), ('Educación Media Incompleta', 'Educación Media Incompleta'), ('Educación Superior Completa', 'Educación Superior Completa'), ('Educación Superior Incompleta', 'Educación Superior Incompleta')], max_length=100),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre_completo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='salud',
            field=models.CharField(choices=[('tramoa', 'TRAMO A'), ('tramob', 'TRAMO B'), ('tramoc', 'TRAMO C'), ('tramod', 'TRAMO D')], max_length=50),
        ),
    ]
