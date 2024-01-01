from . import views
from django.urls import path

app_name='schoolapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/', views.login,name='login'),
    path('register/', views.register,name='register'),
    path('middle/',views.middle,name='middle'),
    path('form/',views.form,name='form'),
    path('final/',views.final,name='final'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),

]