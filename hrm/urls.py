from django.contrib import admin
from django.urls import path

from hrm.apis import EmployeeList, EmployeeDetail, UserAuthentication

app_name = "hrm"

urlpatterns = [
	path('employees/', EmployeeList.as_view(), name='employees_list'),	
	path('employee/<int:employee_id>', EmployeeDetail.as_view(), name='employee_detail'),
	path('auth/', UserAuthentication.as_view(), name="user_auth_token_api")	
]