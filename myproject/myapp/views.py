from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt

# Vista para obtener una lista de empleados con campos específicos
def employee_list(request):
    """
    Devuelve una lista de empleados con los campos 'name', 'age' y 'department'.
    """
    employees = Employee.objects.all().values('name', 'age', 'department')
    return JsonResponse(list(employees), safe=False)

# API para obtener una lista de empleados serializados
@api_view(['GET'])
def api_employee_list(request):
    """
    Devuelve una lista de empleados serializados en formato JSON.
    """
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# API para crear una nueva cita
@api_view(['POST'])
def create_appointment(request):
    """
    Crea una nueva cita a partir de los datos proporcionados en la solicitud.
    """
    serializer = EmployeeSerializer(data=request.data)  # Cambiar a un serializer de citas
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Cita creada correctamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API para listar todas las citas
@api_view(['GET'])
def list_appointments(request):
    """
    Devuelve una lista de todas las citas.
    """
    appointments = Employee.objects.all()  # Cambiar a un modelo de citas
    serializer = EmployeeSerializer(appointments, many=True)  # Cambiar a un serializer de citas
    return Response(serializer.data)

# API para eliminar una cita por su ID
@api_view(['DELETE'])
def delete_appointment(request, id):
    """
    Elimina una cita específica por su ID.
    """
    try:
        appointment = Employee.objects.get(id=id)  # Cambiar a un modelo de citas
        appointment.delete()
        return Response({"message": "Cita eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:  # Cambiar a un modelo de citas
        return Response({"error": "Cita no encontrada"}, status=status.HTTP_404_NOT_FOUND)

# API para crear un nuevo empleado
@api_view(['POST'])
def create_employee(request):
    """
    Crea un nuevo empleado a partir de los datos proporcionados en la solicitud.
    """
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API para obtener una lista de empleados (sin protección CSRF)
@csrf_exempt
@api_view(['GET'])
def get_employees(request):
    """
    Devuelve una lista de empleados serializados en formato JSON.
    """
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

# API para actualizar un empleado por su ID
@api_view(['PUT'])
def update_employee(request, id):
    """
    Actualiza los datos de un empleado específico por su ID.
    """
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response({"error": "Empleado no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API para eliminar un empleado por su ID
@api_view(['DELETE'])
def delete_employee(request, id):
    """
    Elimina un empleado específico por su ID.
    """
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response({"message": "Empleado eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:
        return Response({"error": "Empleado no encontrado"}, status=status.HTTP_404_NOT_FOUND)
