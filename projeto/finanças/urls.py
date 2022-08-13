from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name='finanças'
urlpatterns =[
    path('',views.index,name='index'),
    #Principal view
    path('inicio/', views.PrincipalView.as_view(), name='principal'),
    




]