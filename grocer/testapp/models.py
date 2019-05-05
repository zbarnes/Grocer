from django.db import models

class Organization(models.Model):
    name = models.CharField(unique=True, max_length=255)
    addr = models.CharField(unique=True, max_length=255)
    foods = models.ManyToManyField('Food_Requested')
    status = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
class Food_Requested(models.Model):
    name = models.CharField(max_length=250)
    #originator = models.PrimaryKey('Requester', on_delete=models.SET_NULL)
    '''type = models.CharField(max_length=250)
    quantity_weight = models.IntegerField()
    quantity_unit = models.IntegerField()
    isPerishable = models.BooleanField()
    isVegetarian = models.BooleanField()
    isVegan = model.BooleanField()
    containsDairy = models.BooleanField()
    containsNuts = models.BooleanField()
    containsSeafood = models.BooleanField()
    containsGluten = models.BooleanField()
    quantity_requested = models.IntegerField()
    requested_time = models.DateField()
    '''
'''
class Food_Produced(models.Model):
    name = models.CharField(max_length=250)
    originator = models.PrimaryKey('Producer', on_delete=models.SET_NULL)
    type = model.CharField(max_length=250)
    quantity_weight = models.Integer()
    quantity_unit = models.Integer()
    isPerishable = models.BooleanField()
    isVegetarian = models.BooleanField()
    isVegan = models.BooleanField()
    containsDairy = models.BooleanField()
    containsNuts = models.BooleanField()
    containsSeafood = models.BooleanField()
    containsGluten = models.BooleanField()
    expiration_date = models.DateField()
    produced_date = models.DateField()
    quantity_weight = models.Integer(null=true)
    quantity_unit = models.Integer()

class Producer(models.Model):
    name = models.CharField(max_length=250)
    county = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    zip = models.CharField(max_length=5)
    email = models.EmailField(max_length=250, unique=true)
    phone = models.CharField(max_length=10, unique=true)
    website = models.CharField(max_length=250)
    start_Time = models.DateField()
    close_Time = models.DateField()
#    repeatable = models.BooleanField()
#    interval = models.CharField(max_length=50)

class Requester(models.Model):
    name = models.CharField(max_length=250)
    county = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    zip = models.CharField(max_length=5)
    email = models.EmailField(max_length=250, unique=true)
    phone = models.CharField(max_length=10, unique=true)
    website = models.CharField(max_length=250)
    open_time = models.TimeField(auto_now=false, auto_add_now=false)
    operation_days = models.DateField()
    gender_served = models.CharField(max_length=10)
    ethnicity_served = models.CharField(max_length=50)
    age_served = models.IntegerField()

class Cater(models.Model):
    name = models.OneToOneField('Producer', on_delete=models.SET_NULL)
    max_people_served = models.IntegerField()

class Grocery(models.Model):
    name = models.OneToOneField('Producer', on_delete=models.SET_NULL)

class Restaurant(models.Model):
    name = models.OneToOneField('Producer', on_delete=models.SET_NULL)

class Foodbank(models.Model):
    name = models.OneToOneField('Producer', on_delete=models.SET_NULL)
    start_date = models.DateField()
    close_date = models.DateField()
    service_days = models.DateField()
    gender_served = models.CharField(max_length=10)
    ethnicity_served = models.CharField(max_length=50)
    age_served = models.IntegerField()
    requested_time = models.DateField()

class Shelter(models.Model):
    name = models.OneToOneField('Producer', on_delete=models.SET_NULL)
    '''
