from django.shortcuts import render
from django.http import HttpResponse
from .models import Miner
from django.contrib.auth.decorators import login_required

from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

@login_required(login_url="/accounts/login")
def index(request):
	miners = Miner.objects.all()
	context = {
		'miners': miners,
	}
	# return HttpResponse("test index")
	return render(request, 'miner/index.html', context)

class miner_pool(APIView):

	def get(self, request):
		miners = serializers.serialize("json",Miner.objects.all())
		return Response(miners, status=200)
