from django.urls import path
from .views import lista_estudiantes, lista_profesores, lista_cursos

urlpatterns = [
	path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
  path('profesores/', lista_profesores, name='lista_profesores'),
  path('cursos/', lista_cursos, name='lista_cursos'),
]
