from django.db import models
import datetime

# Create your models here.
class Archive(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    group = models.CharField(max_length=200)
    url   = models.CharField(max_length=250)
    api   = models.CharField(max_length=250)
    history = models.CharField(max_length=250)

#4
class agriculture(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class coal(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class oil_gas(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class metal_ores(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#8
class other_mines(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class textiles(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class wood(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class paper(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#12
class printz(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class pet_products(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class plastic(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class elec_computer(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#16
class basic_metal(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class metal_products(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class equipment(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class electrical(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#20
class comm_devices(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class cars(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class sugar(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class multidisciplinary(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    
