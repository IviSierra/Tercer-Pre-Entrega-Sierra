# Tercer-Pre-Entrega-Sierra

**Para ejecutar la pagina en entorno visual studio code:**

1. **Abrir el IDE.**
2. **Cargar la carpeta "TercerPre-EntregaSierra" a los proyectos de visual.**
3. **Asegurarse en la terminal de estar ubicado en la carpeta "gym_project" que se encuentra dentro de "TercerPre-EntregaSierra".**
4. **Una vez ubicado en la carpeta, ingresar el comando `python manage.py migrate` aplicamos migraciones para la base de datos.**
5. **Ponemos en funcionamiento el servidor con `python manage.py runserver`.**
6. **Ingresa a `http://127.0.0.1:8000` para poder ver la página y probar las funcionalidades.**



## Descripción de archivos

- **static/**: Archivos estáticos como CSS e imágenes.
  - **css/**: Hojas de estilo CSS.
    - `style.css`: Hoja de estilo principal.
  - **img/**: Imágenes.
    - `banner.png`: Imagen de banner.

- **templates/**: Plantillas HTML.
  - `entrenador_form.html`: Formulario de entrenador.
  - `index.html`: Página de inicio.
  - `registro_form.html`: Formulario de registro.
  - `contacto_form.html`: Formulario de contacto.

- `forms.py`: Formularios de la aplicación.
- `models.py`: Modelos de datos.
- `views.py`: Vistas de la aplicación.
- `__init__.py`: Archivo de inicialización.
- `admin.py`: Configuración del administrador.
- `apps.py`: Configuración de la aplicación.
- `tests.py`: Pruebas de la aplicación.
- **migrations/**: Migraciones de base de datos.
  - `0001_initial.py`: Migración inicial.
  - `0002_alter_contacto_telefono_alter_entrenador_horario.py`: Alteración de campos.
  - `0003_rename_telefono_contacto_telefono_contacto`: Renombrado de campos.

