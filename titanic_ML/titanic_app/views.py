from django.shortcuts import render
from rest_framework import viewsets
from .models import Titanic
from titanic_app.serializers import TitanicSerializer
from titanic_app import TiML
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
class TitanicViewset(viewsets.ModelViewSet):
    queryset = Titanic.objects.all().order_by('-id')
    serializer_class = TitanicSerializer

    def create(self, request, *args, **kwargs):
        viewsets.ModelViewSet.create(self,request,*args,**kwargs)
        ob = Titanic.objects.latest('id')
        sur = TiML.pred(ob)
        return Response({'status':'Success','Survived':sur,'tmp':args})
