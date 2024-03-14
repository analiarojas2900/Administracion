from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', 'previous_migration'), # Reemplaza 'previous_migration' con el nombre de la última migración existente en tu aplicación 'core'
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='certificado_presentado_afp',
            field=models.FileField(upload_to='certificados_afp/', default=""),
        ),
    ]