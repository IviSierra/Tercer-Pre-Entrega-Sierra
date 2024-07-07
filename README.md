# Tercer-Pre-Entrega-Sierra

**Para ejecutar la pagina en entorno visual studio code:**

1. **Abrir el IDE.**
2. **Cargar la carpeta "TercerPre-EntregaSierra" a los proyectos de visual.**
3. **Asegurarse en la terminal de estar ubicado en la carpeta "gym_project" que se encuentra dentro de "TercerPre-EntregaSierra".**
4. **Una vez ubicado en la carpeta, ingresar el comando `python manage.py migrate` aplicamos migraciones para la base de datos.**
5. **Ponemos en funcionamiento el servidor con `python manage.py runserver`.**
6. **Ingresa a `http://127.0.0.1:8000` para poder ver la página y probar las funcionalidades.**

**Contenido de los archivos:**

- **gym_app/models.py:** En este archivo definimos los modelos, los cuales definen la estructura de los datos almacenados. Por ejemplo en este caso, definimos los modelos para inscripción, entrenador y contacto.
- **gym_app/forms.py:** En este archivo definimos los formularios para los modelos.
- **gym_app/views.py:** En este archivo definimos las vistas.
- **gym_project/urls.py:** En este archivo definimos las rutas.
- **settings.py:** En este archivo se encuentra la configuración para los archivos estáticos.

**Orden de los archivos:**



gym_project/
│
gym_app/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       └── banner.png
│
├── templates/
│   ├── entrenador_form.html
│   ├── index.html
│   ├── registro_form.html
│   └── contacto_form.html
│
├── forms.py
├── models.py
├── views.py
├── __init__.py
├── admin.py
├── apps.py
├── tests.py
├── __pycache__/
└── migrations/
    ├── __pycache__/
    ├── __init__.py
    ├── 0001_initial.py
    ├── 0002_alter_contacto_telefono_alter_entrenador_horario.py
    └── 0003_rename_telefono_contacto_telefono_contacto

