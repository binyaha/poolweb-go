from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

class Pool(models.Model):
	name = models.CharField(max_length=200)
	para1 = models.CharField(max_length=200)
	para2 = models.CharField(max_length=200)
	para3 = models.CharField(max_length=200)
	para4 = models.CharField(max_length=200)
	para5 = models.CharField(max_length=200)
	para6 = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Miner(models.Model):
	name = models.CharField(max_length=100)
	para1 = models.CharField(max_length=200)
	owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	pool = models.ManyToManyField(Pool, through = 'PoolMux')

	def __str__(self):
		return self.name

class PoolMux(models.Model):
	miner = models.ForeignKey(Miner,on_delete=models.CASCADE,default=None)
	pool =  models.ForeignKey(Pool,on_delete=models.CASCADE,default=None)

# class PoolSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Pool
#         fields = ('name', 'para1','para2')

class MinerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Miner
        fields = '__all__'
