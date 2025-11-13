from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    # autor = models.CharField(max_length=60)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    cuerpo = models.TextField()
    email =  models.CharField(default='xjlundel035@ieshnosmachado.es')


#Se puede utilizar on delete=models.cascada y ...


    def __str__(self):
        return f'autor: ({self.autor}) titulo: {self.titulo}'
    

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    edad= models.IntegerField(null = True, blank= True)

    def __str__(self):
        return self.nombre
    


