from django.urls import path
from .views import employee_list, api_employee_list, create_appointment, list_appointments, delete_appointment, get_employees, create_employee, update_employee, delete_employee

urlpatterns = [
    path('employees/', employee_list, name='employee_list'),
    path('employees/', api_employee_list, name='api_employee_list'),
    path('citas/', create_appointment, name='create_appointment'),
    path('citas/list/', list_appointments, name='list_appointments'),  # Cambiado para evitar conflicto
    path('citas/<int:id>/', delete_appointment, name='delete_appointment'),

    # CRUD para empleados
    path('employees/', get_employees, name='get_employees'),
    path('employees/create/', create_employee, name='create_employee'),
    path('employees/<int:id>/update/', update_employee, name='update_employee'),
    path('employees/<int:id>/delete/', delete_employee, name='delete_employee'),
]
