from django.urls import path
from . import views

urlpatterns = [

    path('', views.course, name='course'), 
    path('modules/',views.modules_view,name="modules")



]