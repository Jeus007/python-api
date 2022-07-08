from django.contrib import admin
from django.urls import path, include

# from django.conf.urls import url


# from hrm.apis import EmployeeList 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hrm.urls'))
    # path('api/employees/', EmployeeList.as_view(), name='employees_list'),
    # url(r'^api/employees/$', EmployeeList.as_view(), name='employees_list')
]
