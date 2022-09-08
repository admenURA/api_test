from email.message import Message
from urllib import response
from django.shortcuts import render
import requests
import datetime
from ServiceAPI import settings

# Create your views here.
from django.http import HttpResponse

from .models import Clients, Mailing, Massege
  
def mailing(request):
    return render(request, "mailing.html")

def client(request):
    return render(request, "client.html")

def createclient(request):
    phonenumber = request.GET.get("phonenumber")
    tegclient = request.GET.get("tegclient")
    codclient = request.GET.get("codclient")
    timezonclient = request.GET.get("timezonclient")
    addclient = Clients.objects.create( phonenumber = phonenumber,
                                        codmail = codclient,
                                        tagmail = tegclient,
                                        timezoneclient = timezonclient)
    return render(request, "client.html")

def startmailing(request):
    

    firstdatemail = request.GET.get("firstdatemail")
    tegcod = request.GET.get("tegcod")
    messagemail = request.GET.get("messagemail")
    seconddatemail = request.GET.get("seconddatemail")
    addmailing = Mailing.objects.create( messagemail = messagemail,
                                         firstdatemail = firstdatemail,
                                         seconddatemail = seconddatemail,
                                         tagmail = tegcod )
    token = settings.TOKEN
    url = settings.URL

    headers = {"accept": "application/json", "Authorization": token , "Content-Type": "application/json"}
    
    #numberclient = Clients.objects.count()
    idmailing = 0
    listclient = Clients.objects.in_bulk()
    for id in listclient:
        if str(listclient[id].tagmail) == tegcod or str(listclient[id].codmail) == tegcod :
            maxmessage = Massege.objects.count()
            goid = Massege.objects.count() + 1
            data = { "id": goid,
                     "phone": listclient[id].phonenumber,
                     "text": messagemail
                    }
            responsemailing = requests.post(url + str(goid), headers=headers, json=data)
            addmessage = Massege.objects.create(starttime = datetime.datetime.now(),
                                                status = responsemailing.status_code,
                                                idmailing = Mailing.objects.count(),
                                                idclient = id )

        
    
    return render(request, "mailing.html")
