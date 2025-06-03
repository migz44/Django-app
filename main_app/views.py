from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.models import Student
from main_app.serializer import StudentSerializer


# Create your views here.

@api_view(['POST'])
def save(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def fetch(request):
    Student.objects.create(names="Tang Lee", email="Leee@test.com", password="<PASSWORD>", gender="male", sports="Football", education="UNIVERSITY")
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
