from django.shortcuts import redirect, render, get_object_or_404
from .models import Libro, Autor, Editorial
from .forms import EditorialForm, AutorForm


def index(request):
    return render(request, 'AppCoder1/index.html')


#Para entregable 19 mayo



def editoriales_formulario(request):

    if request.method == "POST":
        mi_formulario = EditorialForm(request.POST) 

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            editorial = Editorial(nombre = datos["nombre"])
            editorial.save()
            return render(request, 'AppCoder1/editoriales_formulario.html')

    return render(request, 'AppCoder1/editoriales_formulario.html')
            
def autores_formulario(request):

    if request.method == "POST":
        mi_formulario = AutorForm(request.POST) 

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            autor = Autor(nombre = datos["nombre"], apellido = datos["apellido"])
            autor.save()
            return render(request, 'AppCoder1/autores_formulario.html')

    return render(request, 'AppCoder1/autores_formulario.html')


def libros_formulario(request):
    if request.method == "POST":
        try:
            titulo = request.POST["titulo"]
            autor_id = request.POST["autor"]
            editorial_id = request.POST["editorial"]
            fecha_publicacion = request.POST["fecha_publicacion"]
            
            autor = Autor.objects.get(id=autor_id)
            editorial = Editorial.objects.get(id=editorial_id)
            
            libro = Libro(titulo=titulo, autor=autor, editorial=editorial, fecha_publicacion=fecha_publicacion)
            libro.save()
            
            return render(request, 'AppCoder1/libros_formulario.html', {
                'autores': Autor.objects.all(),
                'editoriales': Editorial.objects.all()
            })
        except (Autor.DoesNotExist, Editorial.DoesNotExist):
            # Esto es por si no existe editorial o autor
            return render(request, 'AppCoder1/libros_formulario.html', {
                'autores': Autor.objects.all(),
                'editoriales': Editorial.objects.all(),
                'error': 'Autor o Editorial no encontrados'
            })
    
    return render(request, 'AppCoder1/libros_formulario.html', {
        'autores': Autor.objects.all(),
        'editoriales': Editorial.objects.all()
    })

def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, 'AppCoder1/listado_libros.html', {'libros': libros})




##