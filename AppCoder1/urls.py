from django.urls import path
from .views import listado_libros, libros_formulario, autores_formulario, editoriales_formulario, index

app_name = 'AppCoder1'

urlpatterns = [
    path("", index, name="index" ),

    ##Para entregable 19 mayo
    path('editoriales/', editoriales_formulario, name='editoriales_formulario'),
    path('autores/', autores_formulario, name='autores_formulario'),
    path('libros/', libros_formulario, name='libros_formulario'),
    path('listadolibros/', listado_libros, name='listado_libros'),

    ##
]