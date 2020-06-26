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

#1-4
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

#5-8
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

#9-12
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

#13-16
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

#17-20
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

#21-24
class supply_elec_gas(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class food(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class drug(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class chemical(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#25-28
class contracting(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class wholesale(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class retail(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class tile(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#29-32
class cement(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class non_metal(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class hotel(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class investments(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#33-36
class banks(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class other_financial(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class transportation(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class water_transportation(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#37-40
class financial(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class insurance(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class auxiliary(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class etf(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#41-44
class financing_bonds(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class estate(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class engineering(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class app_computer(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

#45-47
class information(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class technical_services(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

class artistic(models.Model):
    name  = models.CharField(max_length=100)
    kind  = models.CharField(max_length=100)
    date  = models.DateField(default=datetime.date.today)
    data  = models.TextField()    

