from rest_framework import serializers
from .models import Employee  # Cambia a un modelo de citas

class EmployeeSerializer(serializers.ModelSerializer):  # Cambia a un serializer de citas
    class Meta:
        model = Employee  # Cambia a un modelo de citas
        fields = ['id', 'name', 'age', 'department']  # Cambia los campos según el modelo de citas
