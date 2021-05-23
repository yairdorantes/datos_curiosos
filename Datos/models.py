from django.db import models

class Dato(models.Model):
    autor = models.CharField(blank=True,null=True,max_length=10,verbose_name='Autor')
    contenido = models.TextField(blank=False,max_length=370,verbose_name='Contenido')
    imagen = models.ImageField(blank=True,verbose_name='Imágen',upload_to='Datosimg')
    update = models.DateTimeField(auto_now_add=True,verbose_name='Fecha alta',null=True)
    allow = models.BooleanField(default=False,verbose_name='Autorizado')
 
    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(*args, **kwargs)
    class meta:
        db_table = 'Datos'
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
        ordering = ['id']
    def __str__(self):
        return str(self.id)

 
