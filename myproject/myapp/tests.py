from django.test import TestCase
from .models import Employee

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(name="John Doe", age=30, department="HR")

    def test_employee_creation(self):
        john = Employee.objects.get(name="John Doe")
        self.assertEqual(john.age, 30)
