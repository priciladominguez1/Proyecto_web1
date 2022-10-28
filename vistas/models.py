from django.db import models

# Create your models here.
class restaurantes(models.Model):
    id_restaurante = models.AutoField(primary_key=True)
    nombre = models.CharField("nombre", max_length=100, blank = True, null = True)
    estado = models.CharField("estado", max_length=50, blank = True, null = True)
    direccion = models.CharField("direccion", max_length=200, blank = True, null = True)
    tipodecomida = models.CharField("tipodecomida", max_length=100, blank = True, null = True)
    def __str__(self):
        return self.nombre
