from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre       = models.CharField(max_length=200)
    apellidos    = models.CharField(max_length=200)
    status       = models.BooleanField(default=True)

    def __unicode__(self):
        nombrecompleto = "%s %s" %(self.nombre, self.apellidos)
        return nombrecompleto
