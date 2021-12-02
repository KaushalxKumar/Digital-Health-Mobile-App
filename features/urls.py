from django.urls import path
from features.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name="logout"),
    path('make-an-appointment/', AppointmentTemplateView.as_view(), name='appointment'),
    path('manage-appointments/', ManageAppointmentTemplateView.as_view(), name='manage'),
]
