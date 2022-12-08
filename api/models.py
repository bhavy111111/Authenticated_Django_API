from django.db import models

# Create Company Models

class Company(models.Model):
    t = (('IT'  , 'IT') , ('FIN' ,'FIN') , ('NONIT','NOTIT')) 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=t)
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Employee Model

class Employee(models.Model):
    ts = (('Manager'  , 'Manager') , ('Software Developer' ,'SD1') , ('Project Lead','PL'))
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.CharField(max_length=100)
    position = models.CharField(max_length=50 , choices = ts)
    #Relationship between company and employee (1 to many)
    company =  models.ForeignKey(Company,on_delete=models.CASCADE)


