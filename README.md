# Aplicación de Gestión de Libros

Esta aplicación web permite agregar libros, autores y editoriales.

## Requisitos

- Python
- Django

## Instalación

1. Clonar el repositorio desde github:
```bash
git clone <url-del-repositorio>
cd PythonProyecto1
```

2. Crea y activa un entorno virtual:
```bash
python -m venv appcoder
source appcoder/bin/activate  # Como lo hice en una mac el codigo es ese
```

3. Instala las librerias usadas en la aplicacion:
```bash
pip install -r reqiurements.txt
```
4. Para crear las tablas en base a los modelos:
```bash
#Para crear las migraciones, se puede ver en el archivo 0001_initial.py de /migrations
python manage.py makemigrations
```

5. Aplica las migraciones de los modelos y se podra ver la base de datos:
```bash
python manage.py migrate
```


6. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

## Estructura del Proyecto

- **AppCoder1**: Aplicación principal que contiene los modelos, vistas y plantillas.
- **MiProyecto**: Configuración del proyecto Django.

## Funcionalidades y Cómo Probarlas

### 1. Página de Inicio

- **URL**: [http://127.0.0.1:8000/AppCoder1/](http://127.0.0.1:8000/AppCoder1/)
- **Descripción**: Página principal con enlaces a las diferentes secciones de la aplicación.

### 2. Gestión de Libros

#### Listado de Libros
- **URL**: [http://127.0.0.1:8000/AppCoder1/listadolibros/](http://127.0.0.1:8000/AppCoder1/listadolibros/)
- **Descripción**: Muestra una tabla con todos los libros registrados en la base de datos.
- **Funcionalidades**:
  - Ver todos los libros con sus detalles (título, autor, editorial, fecha de publicación)
  - Enlaces para agregar nuevos libros, autores y editoriales

#### Formulario de Libros
- **URL**: [http://127.0.0.1:8000/AppCoder1/libros/](http://127.0.0.1:8000/AppCoder1/libros/)
- **Descripción**: Permite agregar nuevos libros a la base de datos.
- **Cómo probar**:
  1. Completa el formulario con los datos del libro
  2. Selecciona un autor y una editorial existentes
  3. Haz clic en "Guardar Libro"
  4. Verifica que el libro aparezca en el listado de libros

### 3. Gestión de Autores

#### Formulario de Autores
- **URL**: [http://127.0.0.1:8000/AppCoder1/autores/](http://127.0.0.1:8000/AppCoder1/autores/)
- **Descripción**: Permite agregar nuevos autores a la base de datos.
- **Cómo probar**:
  1. Completa el formulario con el nombre y apellido del autor
  2. Haz clic en "Guardar Autor"
  3. Verifica que el autor esté disponible al crear un nuevo libro

### 4. Gestión de Editoriales

#### Formulario de Editoriales
- **URL**: [http://127.0.0.1:8000/AppCoder1/editoriales/](http://127.0.0.1:8000/AppCoder1/editoriales/)
- **Descripción**: Permite agregar nuevas editoriales a la base de datos.
- **Cómo probar**:
  1. Completa el formulario con el nombre de la editorial
  2. Haz clic en "Guardar Editorial"
  3. Verifica que la editorial esté disponible al crear un nuevo libro


## Flujo de Trabajo Recomendado

Para probar todas las funcionalidades de la aplicación, se recomienda seguir este orden:

0. Abar en el navegador la siguiente pagina: http://127.0.0.1:8000/AppCoder1/ y siga los siguientes pasos:
1. Crear algunas editoriales usando el formulario de editoriales
2. Crear algunos autores usando el formulario de autores
3. Crear libros seleccionando los autores y editoriales creados previamente
4. Verificar que todos los datos aparezcan correctamente en el listado de libros


## Notas Adicionales

- Aplique algunos CSS generales en la pagina de los formularios y en la plantilla Padre y de index pero me falto agregarlos todos a un solo archivo CSS.

