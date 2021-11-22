from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from features.models import *
from features.forms import *

# Create your views here.
def index(request):
    return render(request, 'login.html')

#Register User:
def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')

    context = {'form' : form}
    return render(request, 'register.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

# # Create Health Professional:
# def create_health_professional(request):
#     response = "ERROR"
#
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         first_name = payload['first_name']
#         last_name = payload['last_name']
#         email = payload['email']
#         password = payload['password']
#         status = payload['status']
#
#         health_professional = healthProfessional(first_name = first_name, last_name = last_name, email = email, password = password, status = status)
#         try:
#             health_professional.save()
#             response = "SUCCESS"
#         except:
#             response = "FAILED"
#
#     return HttpResponse(response)
#
# # Create User :
# def create_user(request):
#     response = "ERROR"
#
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         email = payload['email']
#         password = payload['password']
#         status = payload['status']
#
#         user = User(email = email, password = password, status = status)
#         try:
#             user.save()
#             response = "SUCCESS"
#         except:
#             response = "FAILED"
#
#     return HttpResponse(response)
#
# # Change Password User:
# def change_password_user(request):
#     response = "ERROR"
#
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         email = payload['email']
#         password = payload['password']
#         new_password =payload['new_password']
#
#         user = User.objects.get(email=email)
#         if password == user.password:
#             try:
#                 user.password = new_password
#                 user.save()
#                 response = "VALID"
#
#             except:
#                 response = "INVALID"
#
#     return HttpResponse(response)
#
# # Change Password Health Professional:
# def change_password_health_professional(request):
#     response = "ERROR"
#
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         email = payload['email']
#         password = payload['password']
#         new_password =payload['new_password']
#
#         healh_professional = healthProfessional.objects.get(email=email)
#         if password == healh_professional.password:
#             try:
#                 healh_professional.password = new_password
#                 healh_professional.save()
#                 response = "VALID"
#
#             except:
#                 response = "INVALID"
#
#     return HttpResponse(response)
#
# # Logout User:
# def logout_user(request):
#     response = "ERROR"
#
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         email = payload['email']
#         user = User.objects.get(email=email)
#
#         try:
#             user.status = "offline"
#             user.save()
#             response = "VALID"
#
#         except:
#             response = "INVALID"
#
#     return HttpResponse(response)
#
# # Logout User:
# def logout_health_professional(request):
#     response = "ERROR"
#
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         email = payload['email']
#         health_professional = healthProfessional.objects.get(email=email)
#
#         try:
#             health_professional.status = "offline"
#             health_professional.save()
#             response = "VALID"
#
#         except:
#             response = "INVALID"
#
#     return HttpResponse(response)
#
# # Get Available Health Professionals
# def get_available_health_professionals(request):
#     pass
#
# # Create Appointment:
# def create_appointment(request):
#     response = "ERROR"
#
#     if request.method == 'POST':
#         payload = json.loads(request.body)
#         user_email = payload['user_email']
#         health_professional_email = payload['health_professional_email']
#         date_time = payload['date_time']
#
#         user = User.objects.get(email=user_email)
#         health_professional = healthProfessional.get(email = health_professional_email)
#
#         appointment = Appointment(userID = user.id, professionalID = health_professional.id, date_time = date_time)
#         try:
#             appointment.save()
#             response = "SUCCESS"
#         except:
#             response = "FAILED"
#
#     return HttpResponse(response)
#
# # Retrieve Appointments:
# def get_appointment(request):
#     pass


