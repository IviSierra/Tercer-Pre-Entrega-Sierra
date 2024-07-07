from django.db import models

class Entrenador(models.Model):
    nombre_completo = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class Inscripcion(models.Model):
    nombre_completo = models.CharField(max_length=100)
    edad = models.IntegerField()
    MEMBRESIA_CHOICES = [
        ('vip', 'VIP'),
        ('clasico', 'Clásico'),
    ]
    membresia = models.CharField(max_length=10, choices=MEMBRESIA_CHOICES)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo

class Contacto(models.Model):
    nombre_completo = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=15)
    mail = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre_completo
