from django.urls import re_path
from . import views
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'miner'

urlpatterns = [
    re_path(r'^$', views.index, name = 'index'),
    re_path(r'^apipool', views.miner_pool.as_view(), name='api_pool'),
    # re_path(r'^apipool', views.miner_pool.as_view(), name='api_pool'),
]