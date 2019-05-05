from django.db import models
import datetime

class Organization(models.Model):
    name = models.CharField(unique=True, max_length=255)
    addr = models.CharField(unique=True, max_length=255)
    foods = models.ManyToManyField('Food_Requested')
    status = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
#class Food(models.Model):
    #name = models.CharField(max,length=255)
    
class Food_Requested(models.Model):
    name = models.CharField(max_length=250)
    originator = models.ForeignKey('Requester', default = '', on_delete=models.CASCADE)
    food_type = models.CharField(max_length=250, default = '')
    quantity_weight = models.IntegerField(default=0)
    quantity_unit = models.IntegerField(default=0)
    isPerishable = models.BooleanField(default=False)
    isVegetarian = models.BooleanField(default=False)
    isVegan = models.BooleanField(default=False)
    containsDairy = models.BooleanField(default=False)
    containsNuts = models.BooleanField(default=False)
    containsSeafood = models.BooleanField(default=False)
    containsGluten = models.BooleanField(default=False)
    quantity_requested = models.IntegerField(default=0)
    requested_time = models.DateField(default=datetime.date.today)
    

class Food_Produced(models.Model):
    name = models.CharField(max_length=250)
    originator = models.ForeignKey('Producer', default = '', on_delete=models.CASCADE)
    food_type = models.CharField(max_length=250, default='')
    quantity_weight = models.IntegerField(default=0)
    quantity_unit = models.IntegerField(default=0)
    isPerishable = models.BooleanField(default=False)
    isVegetarian = models.BooleanField(default=False)
    isVegan = models.BooleanField(default=False)
    containsDairy = models.BooleanField(default=False)
    containsNuts = models.BooleanField(default=False)
    containsSeafood = models.BooleanField(default=False)
    containsGluten = models.BooleanField(default=False)
    expiration_date = models.DateField(default=datetime.date.today)
    produced_date = models.DateField(default=datetime.date.today)
    quantity_weight = models.IntegerField(default=0)
    quantity_unit = models.IntegerField(default=0)

class Producer(models.Model):
    name = models.CharField(max_length=250, default='')
    county = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    address = models.CharField(max_length=250, default='')
    zip_code = models.CharField(max_length=5, default='')
    email = models.EmailField(max_length=250, default='')
    phone = models.CharField(max_length=10, default='')
    website = models.CharField(max_length=250, default='')
    start_Time = models.DateField(default=datetime.date.today)
    close_Time = models.DateField(default=datetime.date.today)
#    repeatable = models.BooleanField()
#    interval = models.CharField(max_length=50)

class Requester(models.Model):
    name = models.CharField(max_length=250, default='')
    street = models.CharField(max_length=250, default='')
    county = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip_code = models.CharField(max_length=5, default='')
    email = models.EmailField(max_length=250, default='')
    phone = models.CharField(max_length=10, default='')
    website = models.CharField(max_length=250, default='')
    open_time = models.TimeField()
    close_time = models.TimeField()
    operation_days = models.DateField(default=datetime.date.today)
    

class Cater(models.Model):
    name = models.ForeignKey('Producer',default = '', on_delete=models.CASCADE)
    max_people_served = models.IntegerField(default=0)

class Grocery(models.Model):
    name = models.ForeignKey('Producer',default = '', on_delete=models.CASCADE)

class Restaurant(models.Model):
    name = models.ForeignKey('Producer', default = '',on_delete=models.CASCADE)

class Foodbank(models.Model):
    name = models.ForeignKey('Requester',default = '', on_delete=models.CASCADE)
    #start_date = models.DateField()
    #close_date = models.DateField()
    #service_days = models.DateField()
    

class Shelter(models.Model):
    name = models.ForeignKey('Requester',default = '', on_delete=models.CASCADE)
    gender_served = models.CharField(max_length=255, default='')
    ethnicity_served = models.CharField(max_length=255, default='')
    age_served = models.IntegerField(default=0)
    requested_time = models.DateField(default=datetime.date.today)

