from rest_framework import serializers  # serializer

from main_app.models import Student


class StudentSerializer(serializers.ModelSerializer):
     class Meta:
         model = Student
         fields = '__all__'
