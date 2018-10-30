from django.shortcuts import render
from django.http import HttpResponse
from .models import Miner

# Create your views here.

def index(request):
	miners = Miner.objects.all()
	context = {
		'miners': miners,
	}
	return HttpResponse("test index")
	# return render(request, 'miner/index.html', context)
