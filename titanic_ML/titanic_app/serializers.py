from rest_framework import serializers
from .models import Titanic
from django.contrib.auth.models import User

class TitanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titanic
        fields = ('PassengerId','Pclass','Name','Sex','Age',
                 'SibSp','Parch','Ticket','Fare','Cabin','Embarked' )
        
                  

        