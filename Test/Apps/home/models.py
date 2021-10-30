from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)



class Usuario(models.Model):
    perfil = models.OneToOneField(User, on_delete=models.CASCADE)

    def str(self):
        return self.perfil.username

@receiver(post_save, sender=User)
def crear_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(perfil=instance)

@receiver(post_save, sender=User)
def guardar_usuario(sender, instance, created, **kwargs):
    instance.usuario.save()

    

class Profesion(models.Model):
    profesion=models.CharField(max_length=50)
   
    def __str__(self):
        return '%s ' % (self.profesion)


class FormularioInscripcion(models.Model):
    IDusuario=models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        default=1
    )
    gene =(
        ('M', 'Masculino'),
        ('F','Femenino'),
        ('X','Otro')
    )
    edad=models.CharField(max_length=10)
    sexo=models.CharField(max_length=20, choices=gene)
    IDDepartamentos=models.ForeignKey(
        'Departamento',
        on_delete=models.CASCADE,
        default=1
        )
    dMunicipio=models.CharField(max_length=250)
    Direccion=models.CharField(max_length=250)
    profe= models.ManyToManyField(Profesion)
    fotografiaPersonal=models.FileField(upload_to = "Uploaded Files/")
    cartaRecomendacion=models.FileField(upload_to = "Uploaded Files/")
    cartaLaboral=models.FileField(upload_to = "Uploaded Files/")
    tituloyDiplomas=models.FileField(upload_to = "Uploaded Files/")
    CUI=models.CharField(max_length=15)
    fotografiaDPI=models.FileField(upload_to = "Uploaded Files/")
    fotografiaRTU=models.FileField(upload_to = "Uploaded Files/")
    antecedentespenales=models.FileField(upload_to = "Uploaded Files/")
    antecedentespoliciacos=models.FileField(upload_to = "Uploaded Files/")
    
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s ' % (self.CUI,self.IDusuario)


class UsuarioAdmin(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    email=models.EmailField(max_length = 254)
    puesto=models.CharField(max_length=50)
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.nombre, self.puesto)

class Reuniones(models.Model):
    motivo=models.CharField(max_length=500)
    tipo=models.CharField(max_length=50)
    horaRegisto=models.DateField()
    horaReunion=models.DateField()
    link=models.CharField(max_length=150)
    IDUsuarioAdmin=models.ForeignKey(
        'UsuarioAdmin',
        on_delete=models.CASCADE,
        default=1
        )
    creacion=models.DateField(auto_now_add=True)
    actualizacion=models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.motivo, self.horaReunion)

class Asistencia(models.Model):
    IDUsuario=models.ForeignKey(
        'Usuario',
        on_delete=models.CASCADE,
        default=1
        )
    IDReuniones=models.ForeignKey(
        'Reuniones',
        on_delete=models.CASCADE,
        default=1
        )
 
    def __str__(self):
        return '%s' % (self.IDReuniones)


class DocsEditables(models.Model):
    Contenido=models.TextField(max_length=2000)
    Tipo= models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=500)

    def str(self):
        return '%s ' % (self.Descripcion)


class DocumentosEje(models.Model):
    Contenido=models.FileField(upload_to = "Uploaded Files/",blank=False,default=0)
    Tipo= models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=500)

    def str(self):
        return '%s ' % (self.Descripcion)

class DocContables(models.Model):
    Contenido=models.FileField(upload_to = "Uploaded Files/")
    Tipo= models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=500)
    Guia=models.CharField(max_length=50)

    def str(self):
        return '%s ' % (self.Descripcion)

class Cuestionarios(models.Model):
    Contenido=models.FileField(upload_to = "Uploaded Files/")
    Tipo= models.CharField(max_length=50)
    Descripcion=models.CharField(max_length=500)

    def str(self):
        return '%s' % (self.Descripcion) 
   