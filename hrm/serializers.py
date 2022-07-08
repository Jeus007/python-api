from rest_framework import serializers
from hrm.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
	# while 'put' of updating a record, if providing first_name and employee_id is not required
	first_name = serializers.CharField(required = False)
	employee_id = serializers.CharField(required = False)
	rank = serializers.FloatField(required=False)

	class Meta:
		model = Employee
		fields = "__all__"
		