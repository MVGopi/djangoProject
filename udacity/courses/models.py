from django.db import models

# Create your models here.
class DummyDetails(models.Model):
	Gender_choice=(('male','Male'),('female','Female'))

	name=models.CharField(max_length=200)
	mobile=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	gender=models.CharField(max_length=10, choices=Gender_choice)


	def __str__(self):
		return self.name+'@'+self.mobile+'@'+self.email+'@'+self.gender
		