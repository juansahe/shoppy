from django.db import models

class Provider(models.Model):

    level = (
            ('0', 'Marca'),
            ('1', 'Retail'),
            )
    type_provider = models.CharField(verbose_name="Tipo",max_length=200,choices=level,default='0',)
    web_site= models.CharField( verbose_name="Sitio web",max_length=255,null=True,blank=True)
    name = models.CharField( verbose_name="Nombre",max_length=200)
    description = models.TextField( verbose_name="Descripción",null=True)
    phone_contact= models.CharField( verbose_name="Telefono contacto",max_length=50,null=True,blank=True)
    name_contact = models.CharField( verbose_name="Nombre contacto",max_length=200,null=True,blank=True)
    email_contact = models.CharField( verbose_name="Email contacto",max_length=200 ,null=True,blank=True)
    img = models.ImageField( verbose_name="Logo",upload_to = 'uploads/marks/')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['name']

class Promotion(models.Model):

    name = models.CharField( verbose_name="Nombre",max_length=200)
    description = models.TextField( verbose_name="Descripción",null=True,blank=True)
    img = models.ImageField( verbose_name="Imagen",null=True,upload_to = 'uploads/promotion/')
    provider = models.ForeignKey(Provider,verbose_name="Marca o Retail", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Promoción"
        verbose_name_plural = "Promociones"
        ordering = ['name']


class Bond(models.Model):

    level = (
            ('0', 'Activo'),
            ('1', 'Redimido'),
            )
    name = models.CharField( verbose_name="Nombre",max_length=200)
    description = models.TextField( verbose_name="Descripción")
    value = models.CharField( verbose_name="Valor",max_length=200)
    code = models.CharField( verbose_name="Codigo",max_length=200)
    status = models.CharField( verbose_name="Estado",max_length=200, choices=level,default='0',)
    provider = models.ForeignKey(Provider,verbose_name="Marca o Retail", on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bono"
        verbose_name_plural = "Bonos"
        ordering = ['name']

class Redemption(models.Model):
    pass

