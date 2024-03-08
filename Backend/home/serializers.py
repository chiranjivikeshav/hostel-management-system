from rest_framework import serializers
from django.db import models
from home.models import (Student,Hostel,Unit,Room,Dues)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class RoomSerializer(serializers.Serializer):
    Student = StudentSerializer(null =True)
    class Meta:
        model = Room
        fields = '__all__'

class UnitSerializer(serializers.Serializer):
    Room = RoomSerializer(many = True)
    class  Meta:
        model = Unit
        fields = '__all__'    

class HostelSerializer(serializers.ModelSerializer):
    Units = UnitSerializer(many = True)
    class Meta:
        model = Hostel
        fields = '__all__'