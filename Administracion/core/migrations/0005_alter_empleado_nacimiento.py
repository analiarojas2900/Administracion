# Generated by Django 5.0.1 on 2024-03-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_empleado_banco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='nacimiento',
            field=models.CharField(default='', max_length=100),
        ),
    ]
