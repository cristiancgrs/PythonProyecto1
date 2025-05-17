from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable


def index(request):
    return render(request, 'AppCoder1/index.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    #Estudiante.objects.filter(nombre__icontains='Cristian')

    contexto = {
        'estudiantes': estudiantes
    }
    return render(request, 'AppCoder1/estudiantes_list.html', contexto)

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'AppCoder1/estudiantes_detail.html', {'estudiante': estudiante})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {
        'profesores': profesores
    }
    return render(request, 'AppCoder1/profesores_list.html', contexto)