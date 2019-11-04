from django.db import models

# Create your models here.
class Details(models.Model):
	Gender_choise=(('male','Male'),('female','Female'))
	name=models.CharField(max_length=200)
	age=models.IntegerField()
	email=models.EmailField(max_length=100)
	gender=models.CharField(max_length=50,choices=Gender_choise)

	def __str__(self):
		return self.name+' - '+self.email