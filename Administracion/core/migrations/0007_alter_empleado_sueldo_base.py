# Generated by Django 5.0.1 on 2024-03-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_empleado_sueldo_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sueldo_base',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
