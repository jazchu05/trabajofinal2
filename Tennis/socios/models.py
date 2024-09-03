from django.db import models

"""class Socios(models.Model):
    descripcion=models.CharField(max_length=50,verbose_name="descripcion")
    
    def __str__(self):
      fila=self.descripcion
      return fila"""
    
# Create your models here.
class Socios(models.Model):
    idSocio= models.AutoField(primary_key=True, db_column='id')
    DNI=models.IntegerField(verbose_name="DNI")
    nom = models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fechan=models.DateField(verbose_name="Fecha Nacimiento")
    dire=models.CharField(max_length=50,verbose_name="Direccion")
    cp=models.CharField(max_length=6,verbose_name="codigo postal")
    tel=models.CharField(max_length=12,verbose_name="numero de telefono")
    
    def __str__(self):
        fila=str(self.id)+"-"+str(self.DNI)+"-"+self.nom
        return fila
    


    