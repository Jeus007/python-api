from django.db import models

class Employee(models.Model):
	employee_id = models.CharField(max_length=15, unique=True)
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25, null=True, blank=True) #optional field
	age = models.IntegerField(default=18)
	rank = models.FloatField()

	def __str__(self):
		return self.employee_id + ": " + self.first_name + " " + self.last_name

