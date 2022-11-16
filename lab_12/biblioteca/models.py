from django.db import models
from email.policy import default

# Create your models here.
class Libro(models.Model):
    idLibro = models.AutoField(primary_key=True)
    codigo = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    numpags = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name="Libros"
        verbose_name_plural="Libros"

class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    numUsuario = models.IntegerField(default=0)
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name="Usuarios"
        verbose_name_plural="Usuarios"

class Autor(models.Model):
    idAutor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name="Autores"
        verbose_name_plural="Autores"

class Prestamos(models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    idLibro = models.CharField(max_length=100)
    idUsuario = models.CharField(max_length=100)
    FecPrestamo = models.DateField('Fecha de inicio')
    FecDevolucion = models.DateField('Fecha de fin')
    libro = models.ManyToManyField(Libro,through='LibroPrestamo',blank=True)
    usuario = models.ManyToManyField(Usuario,through='UsuarioPrestamo',blank=True)
    
    def __str__(self):
        return self.idLibro
    
    class Meta:
        verbose_name="Prestamos"
        verbose_name_plural="Prestamos"

class LibroPrestamo(models.Model):
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE,blank=True,null=True)
    prestamo = models.ForeignKey(Prestamos,on_delete=models.CASCADE,blank=True,null=True)

class UsuarioPrestamo(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True,null=True)
    prestamo = models.ForeignKey(Prestamos,on_delete=models.CASCADE,blank=True,null=True)
