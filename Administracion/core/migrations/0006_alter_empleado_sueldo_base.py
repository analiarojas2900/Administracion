# Generated by Django 5.0.1 on 2024-03-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_empleado_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='sueldo_base',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
