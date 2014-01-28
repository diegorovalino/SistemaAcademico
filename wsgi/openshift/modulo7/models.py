# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class Carreras(models.Model):
    cod_carrera = models.IntegerField(primary_key=True)
    nombre_carrera = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'carreras'

class Estados(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    normal = models.TextField(blank=True)
    extension = models.TextField(blank=True)
    anulacion = models.TextField(blank=True)
    class Meta:
        db_table = u'estados'

class Periodos(models.Model):
    id_periodo = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    fechainiper = models.DateField()
    fechafinper = models.DateField()
    fechainian = models.DateField(null=True, blank=True)
    fechafinan = models.DateField(null=True, blank=True)
    fechainiex = models.DateField(null=True, blank=True)
    fechafinex = models.DateField(null=True, blank=True)
    fechainima = models.DateField(null=True, blank=True)
    fechafinma = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'periodos'

class Estudiantes(models.Model):
    ci = models.TextField(primary_key=True)
    cod_carrera = models.ForeignKey(Carreras, null=True, db_column='cod_carrera', blank=True)
    nombre = models.TextField()
    apellido = models.TextField()
    telefono = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    estado = models.BooleanField(null=False, blank=True)
    email = models.TextField(blank=True)
    foto = models.CharField(max_length=254, blank=True)
    tiposangre = models.TextField(blank=True)
    fechagraduacion = models.DateField(null=True, blank=True)
    colegiograduacion = models.TextField(blank=True)
    fechanacimiento = models.DateField(null=True, blank=True)
    notagraduacion = models.IntegerField(null=True, blank=True)
    especialidadgraduacion = models.TextField(blank=True)
    ciudadania = models.TextField(blank=True)
    ciudadnacimiento = models.TextField(blank=True)
    ciudadactual = models.TextField(blank=True)
    provincianacimiento = models.TextField(blank=True)
    provinciaactual = models.TextField(blank=True)
    class Meta:
        db_table = u'estudiantes'
