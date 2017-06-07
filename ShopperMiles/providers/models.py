from django.db import models

class Mark(models.Model):
    # additional fields here
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    phone_contact= models.CharField(max_length=50,null=True)
    name_contact = models.CharField(max_length=200,null=True)
    email_contact = models.CharField(max_length=200 ,null=True)
    img = models.ImageField(upload_to = 'uploads/marks/')
    def __str__(self):
        return self.name

class Retail(models.Model):
    # additional fields here
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    phone_contact= models.CharField(max_length=50,null=True)
    name_contact = models.CharField(max_length=200,null=True)
    email_contact = models.CharField(max_length=200 ,null=True)
    img = models.ImageField(upload_to = 'uploads/retail/')
    def __str__(self):
        return self.name


class Promotion(models.Model):
    # additional fields here
   pass