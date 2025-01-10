# Generated by Django 5.1.4 on 2025-01-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('doctor', 'Doctor'), ('recepcionista', 'Recepcionista'), ('paciente', 'Paciente')], max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
