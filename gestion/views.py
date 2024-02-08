from django.shortcuts import render
from .models import Estudiante, Profesor, Curso

def lista_estudiantes(request):
  estudiantes = Estudiante.objects.all()
  return render(request, 'gestion/lista_estudiantes.html', {'estudiantes': estudiantes})

def lista_profesores(request):
  profesores = Profesor.objects.all()
  return render(request, 'gestion/lista_profesores.html', {'profesores': profesores})

def lista_cursos(request):
  cursos = Curso.objects.all()
  return render(request, 'gestion/lista_cursos.html', {'cursos': cursos})
