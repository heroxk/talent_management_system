from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
  # url(r'^$',views.index,name='index'),
  # url('index_sample',views.index_sample,name='index_sample'),
  url('index',views.index,name='index'),
  url('info_input',views.info_input,name='info_input'),
  url('talent_list',views.talent_list,name='talent_list'),
  url('talent_search',views.talent_search,name='talent_search'),

  # url('first_app',include('first_app.urls')),
  # url(r'^admin/',admin.site.urls)
]
