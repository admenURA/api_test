from email import message
from django.db import models
 
class Mailing(models.Model):
    messagemail = models.TextField()
    firstdatemail = models.DateTimeField()
    seconddatemail = models.DateTimeField()
    tagmail = models.TextField()

class Clients(models.Model):
    phonenumber = models.IntegerField()
    codmail = models.IntegerField()
    tagmail = models.IntegerField()
    timezoneclient = models.IntegerField()

class Massege(models.Model):
    starttime = models.DateTimeField()
    status = models.TextField()
    idmailing = models.IntegerField()
    idclient = models.IntegerField()