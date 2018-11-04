from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Miner
from .models import Miner, Pool, PoolMux
from django.contrib.auth.decorators import login_required
from . import forms

from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

@login_required(login_url="/accounts/login")
def index(request):
	miners = Miner.objects.filter(owner_id=request.user.id)
	context = {
		'miners': miners,
		'user': request.user,
	}
	# return HttpResponse("test index")
	return render(request, 'miner/index.html', context)

class miner_pool(APIView):

	def get(self, request):
		miners = Miner.objects.filter(owner_id=request.GET.get('user', ''))
		minersjson = serializers.serialize("json",{'test': 'qweqwe'})
		# return Response(miners, status=200)
		return HttpResponse(minersjson, status=200)

@login_required(login_url="/accounts/login")
def detail(request, miner_id):
	machine = Miner.objects.get(pk=miner_id)
	pools = Pool.objects.all()
	try:
		pool_mux_id = PoolMux.objects.get(miner=miner_id).pool_id
	except:
		context = {'machine' : machine, 'pools': pools }
	else:
		now_pool = Pool.objects.get(pk=pool_mux_id)
		context = {'machine' : machine, 'pools': pools, 'now_pool': now_pool }
	return render(request, 'miner/miner_detail.html', context)

@login_required(login_url="/accounts/login")
def miner_create(request):
	if request.method == 'POST':
		form = forms.CreateMiner(request.POST)
		if form.is_valid():
			#save article to db
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			return redirect('miner:index')
	else:
		form = forms.CreateMiner()
	return render(request, 'miner/miner_create.html', {'form' : form})

@login_required(login_url="/accounts/login")
def change_pool(request):
	if request.method == 'POST':
		form = forms.CreatePoolMux(request.POST)
		if form.is_valid():
			print('看這裡:', request.POST['pool'])
			try:
				miner = PoolMux.objects.get(miner=request.POST['miner'])
			except:
			  print("no miner")
			  form.save()
			else:
				update_object = PoolMux.objects.filter(miner=request.POST['miner'])
				update_object.update(pool=request.POST['pool'])
		else:
			print('form不對')

	return redirect('miner:index')
