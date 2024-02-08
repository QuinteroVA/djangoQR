from django.db import models

class Estudiante(models.Model):
	cedula = models.CharField(max_length=10)
	nombre = models.CharField(max_length=25)
	apellido = models.CharField(max_length=25)
	direccion = models.CharField(max_length=50)
	correo = models.CharField(max_length=25)

class Profesor(models.Model):
  cedula = models.CharField(max_length=10)
  nombre = models.CharField(max_length=25)
  apellido = models.CharField(max_length=25)
  direccion = models.CharField(max_length=50)
  correo = models.CharField(max_length=25)
class Cursos(models.Model):
  curso = models.CharField(max_length=25)
  profesor = models.CharField(max_length=25)
  materia = models.CharField(max_length=25)
  horario = models.CharField(max_length=25)

  def __str__(self):
    return self.nombre
