from django.db import models
from django.contrib.auth.models import User

class Miner(models.Model):
	name = models.CharField(max_length=200)
	para1 = models.CharField(max_length=200)
	# owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.name