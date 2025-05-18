from django.db import models
from duenos.models import Dueno
from especies.models import Especie

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')])
    dueño = models.ForeignKey(Dueno, on_delete=models.CASCADE, related_name='mascotas')
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
