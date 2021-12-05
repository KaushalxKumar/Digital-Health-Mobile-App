from django.urls import path
from django.contrib import admin
from features.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('on-demand/', available, name='available'),
    path('view-profile/', profile, name='profile'),
    path('make-an-appointment/', AppointmentTemplateView.as_view(), name='appointment'),
    path('manage-appointments/', ManageAppointmentTemplateView.as_view(), name='manage'),

]
