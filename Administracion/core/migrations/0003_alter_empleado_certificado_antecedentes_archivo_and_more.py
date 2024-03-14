# Generated by Django 5.0.1 on 2024-03-14 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_empleado_certificado_antecedentes_archivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='certificado_antecedentes_archivo',
            field=models.FileField(default=None, upload_to='static/img/certificados_antecedentes/'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='certificado_presentado_afp',
            field=models.FileField(default=None, upload_to='static/img/certificados_afp/'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='certificado_presentado_salud_archivo',
            field=models.FileField(default=None, upload_to='static/img/certificados_salud/'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='copia_carnet_archivo',
            field=models.FileField(default=None, upload_to='static/img/copias_carnet/'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='numero_calzado',
            field=models.PositiveSmallIntegerField(choices=[(34, '34'), (35, '35'), (36, '36'), (37, '37'), (38, '38'), (39, '39'), (40, '40'), (41, '41'), (42, '42'), (43, '43'), (44, '44'), (45, '45')], default=34),
        ),
    ]