from django.db import models

# Create your models here.

class Comprador(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email}'
    

class Emprendedor(models.Model):
    nombre = models.CharField(max_length=100)
    emprendimiento = models.CharField(max_length=100)
    dinero_requerido = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.nombre} - {self.emprendimiento} - {self.dinero_requerido}'

class Inversor(models.Model):
    nombre_empresa = models.CharField(max_length=40)
    rubro_empresa = models.CharField(max_length=40)
    capital_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.nombre_empresa} - {self.rubro_empresa} - {self.capital_inicial}'

