'''
This is the client of the RESTful APIs created by using Django Rest API framework.
The API is token-authenticated. Hence, while consuming the APIs, token needs to be passed
A token can be created by providing a valid username and password. This token will then be used to access the APIs
'requests' library is being used here to access the API urls: pip install 'requests'
'''

import requests

class Client:
	def get_auth_token(self):
		# step-1: URL to fetch all the employees
		api_authentication_url = "http://127.0.0.1:8000/api/auth/"

		# step-2: use the 'post' method to provide user credenticals and get back auth token
		response = requests.post(api_authentication_url, data={'username': 'super_admin', 
						 'password': 'testpassword'
						})		
		# return response	==> working
		self.auth_token = response


	# now use the token to access the apis
	# url: "http://127.0.0.1:8000/api/employees/"
	def get_employees(self):		
		#step-1: set the api url 
		api_data_url = "http://127.0.0.1:8000/api/employees/"
		
		#step-2: set the auth token in the header and 
		# 		use the 'get' method now to fetch the employees records using the above api
		# header = { 'Authorization' : 'Token ' + token.json() } 	==> working
		header = {'Authorization' : 'Token ' + self.auth_token.json() }
		data = requests.get(api_data_url, headers = header)

		for emp in data:
			print(emp)


	# url: http://127.0.0.1:8000/api/employee/5
	def get_employee_details(self, employee_id):
		employeee_url = "http://127.0.0.1:8000/api/employee/{}".format(employee_id)
		header = {'Authorization' : 'Token ' + self.auth_token.json() }
		print(employeee_url)

		#fetch record
		emp = requests.get(employeee_url, headers = header)
		print(emp.json())
		return emp.json()


	# create (aka POST) a new employee
	# url: http://127.0.0.1:8000/api/employees/
	def create_employee(self):
		post_url = "http://127.0.0.1:8000/api/employees/"  #post and get urls are same for list of employees
		header = {'Authorization' : 'Token ' + self.auth_token.json() }
		data = {			
	        "first_name": "New User",
	        "employee_id": "em007",
	        "rank": 2.9,
	        "last_name": "Jonek",
	        "age": 30	    
			}
		response = requests.post(post_url, data = data, headers = header)
		print(response.json())


	# edit/modify (ie. PUT) employee data
	# url: http://127.0.0.1:8000/api/employees/5
	def edit_employee(self, employee_id):
		#post and get urls are same for list of employees
		update_url = "http://127.0.0.1:8000/api/employee/{}".format(employee_id)  
		header = {'Authorization' : 'Token ' + self.auth_token.json() }
		data = self.get_employee_details(employee_id)
		
		data = {			
	        "first_name": (data["first_name"] + " updated_from_client_script")
			}
		response = requests.put(update_url, data = data, headers = header)
		print(response.json())
	

	def delete_employee(self, employee_id):
		delete_url = "http://127.0.0.1:8000/api/employee/{}".format(employee_id)
		header = {'Authorization' : 'Token ' + self.auth_token.json() }

		response = requests.delete(delete_url, headers = header)
		print(response.status_code)

client = Client()
client.get_auth_token()
# client.get_employees()
client.create_employee()
# client.get_employee_details(5)
# client.edit_employee(5)
# client.delete_employee(8)



