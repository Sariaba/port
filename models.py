from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=122)
	email = models.CharField(max_length=122)
	phone_no = models.CharField(max_length=12)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name