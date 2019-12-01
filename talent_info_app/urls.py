from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
  url(r'^$',views.index,name='index'),
  url('info_input',views.info_input,name='info_input'),
  url('talent_list',views.talent_list,name='talent_list'),
  # url('first_app',include('first_app.urls')),
  # url(r'^admin/',admin.site.urls)
]
