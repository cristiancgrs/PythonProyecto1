
from django import forms
from .models import Editorial, Autor, Libro

class EditorialForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    
    class Meta:
        model = Editorial
        fields = '__all__'


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'fecha_publicacion']
