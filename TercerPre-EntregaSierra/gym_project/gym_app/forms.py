from django import forms
from .models import Inscripcion, Entrenador, Contacto

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['nombre_completo', 'edad', 'membresia', 'entrenador']

class EntrenadorForm(forms.ModelForm):
    HORARIO_CHOICES = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche'),
    ]
    horario = forms.ChoiceField(choices=HORARIO_CHOICES)

    class Meta:
        model = Entrenador
        fields = ['nombre_completo', 'horario']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_completo', 'telefono_contacto', 'mail', 'mensaje']
