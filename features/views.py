from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

from features.models import *
from features.forms import *
from django.db.models.query import QuerySet

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('dashboard')

        context = {'form' : form}
        return render(request, 'register.html', context)
def forgetPassword(request):
    return render(request, 'forgetPassword.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def available(request):
    professionals = Person.objects.filter(professional=True, on_demand=True)
    rooms = ChatRoom.objects.all()
    return render(request, 'on-demand.html', {'professionals': professionals, 'rooms' : rooms})



class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def get(self, request):
        professionals = Person.objects.filter(professional=True)
        return render(request, 'appointment.html', {'professionals': professionals})

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")
        professional= request.POST.get("professional")

        appointment = Appointment.objects.create(
            health_professional_username = professional,
            user_username = request.user.username,
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS,
                             f"Thanks {fname} for making an appointment, we will email you the link to join the meeting once its confirmed")
        return HttpResponseRedirect(request.path)


class EditProfileView(TemplateView):
    login_required = True
    template_name = "profile.html"

    def post(self, request):
        user = Person.objects.get(username=request.user.username)
        answer = request.POST.get("preference")
        if answer == "Agree":
            user.on_demand = True
        else:
            user.on_demand = False

        user.save()
        messages.add_message(request, messages.SUCCESS, f"Your preference was changed")

        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        time = request.POST.get("appt")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        chat = ChatRoom.objects.all()

        data = {
            "professional": request.user.username,
            "fname": appointment.first_name,
            "date": date,
            "chat": chat,
            "time" : time,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [request.user.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment for {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.professional:
            appointments = Appointment.objects.filter(health_professional_username=self.request.user.username)

        else:
            appointments = Appointment.objects.filter(user_username=self.request.user.username)

        context.update({
            "title": "Manage Appointments"
        })
        return context
    