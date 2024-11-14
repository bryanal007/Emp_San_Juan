# Generated by Django 5.1.3 on 2024-11-14 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True, unique=True)),
                ('ubicacion', models.CharField(max_length=100, null=True)),
                ('presupuesto', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('nombre', models.CharField(max_length=30, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('cedula', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('celular', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_evaluacion', models.DateField(null=True)),
                ('puntaje', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('comentarios', models.TextField(blank=True, max_length=500, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Conemp.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa_anterior', models.CharField(max_length=100, null=True)),
                ('puesto_anterior', models.CharField(max_length=50, null=True)),
                ('fecha_inicio', models.DateField(null=True)),
                ('fecha_fin', models.DateField(null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Conemp.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Conemp.departamento')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Conemp.puesto'),
        ),
    ]
