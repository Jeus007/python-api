from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from hrm.models import Employee
from hrm.serializers import EmployeeSerializer


'''
this class is used to authenticate user credentials received by any client script 
and return the auth token. 
this auth token is then used by that client script to access the APIs

as the script sends username and password over the internet, hence only 'post' 
method is supported for authentication
'''
class UserAuthentication(ObtainAuthToken):
	def post(self, request, *args, **kwargs) :
		serializer = self.serializer_class(data=request.data, context={'request' : request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user'] 
		token, created = Token.objects.get_or_create(user=user)
		return Response(token.key)


'''
all the REST methods will be implemented as part of the below class
the "APIView" method from rest_framework.views file expects the implementation of these methods
note: this class will take care of listing employees and creating a new employee
supporting urls: 
	/api/employees
'''
class EmployeeList(APIView):
	#get method
	def get(self, request):
		#return all the employees in 'serialized' form
		model = Employee.objects.all()
		serializer = EmployeeSerializer(model, many=True)
		return Response(serializer.data)

	#post method: this is to create a new employee
	def post(self, request):
		serializer = EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			#save the new record
			serializer.save()

			#show the newly created record
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# note: this class will take care of showing details of one employee and updating it
# supporting urls: 
	# /api/employee/1
class EmployeeDetail(APIView):

	# helper method to get a model (aka, employee object)
	def get_an_employee(employee_id):
		try:
			employee_object = Employee.objects.get(id = employee_id)
		except Employee.DoesNotExist:		
			return None
		else:
			return employee_object


	#get method
	def get(self, request, employee_id):
		# search for the employee_id in the database
		model = EmployeeDetail.get_an_employee(employee_id)
		if model is None:
			return Response("Employee with id:{} Does not exist".format(employee_id), status = status.HTTP_404_NOT_FOUND)
				
		#serialize the data, meaning covert the database object in understandable format by python
		serializer = EmployeeSerializer(model)
		return Response(serializer.data, status = status.HTTP_200_OK)
		

	#post method
	def put(self, request, employee_id):
		# get the model which needs to be updated in a form
		model = EmployeeDetail.get_an_employee(employee_id)
		if model is None:
			return Response("Employee with id:{} Does not exist".format(employee_id), status = status.HTTP_404_NOT_FOUND)

		# if model is valid, then updation is possible
		serializer = EmployeeSerializer(model, data=request.data)		
		if serializer.is_valid():
			#save the new record
			serializer.save()

			#show the newly created record
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	# delete method
	def delete(self, request, employee_id):
		model = EmployeeDetail.get_an_employee(employee_id)
		if model is None:
			return Response("Employee with id:{} Does not exist".format(employee_id), status = status.HTTP_404_NOT_FOUND)
		
		model.delete()
		return Response("Removed Employee with id: {}".format(employee_id), status=status.HTTP_204_NO_CONTENT)
