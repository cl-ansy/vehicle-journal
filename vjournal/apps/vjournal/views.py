from django import forms
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from vjournal.apps.vjournal.models import Vehicle
from vjournal.apps.vjournal.models import Part
from vjournal.apps.vjournal.models import Mechanic
from vjournal.apps.vjournal.models import History
from vjournal.apps.vjournal.models import Finance
from vjournal.apps.vjournal.forms import VehicleForm
from vjournal.apps.vjournal.forms import PartForm
from vjournal.apps.vjournal.forms import MechanicForm
from vjournal.apps.vjournal.forms import HistoryForm
from vjournal.apps.vjournal.forms import FinanceForm


@login_required(login_url='/account/login/')
def index(request):
    #get all the vehicles that belong to the user that is logged in to create
    #a list of vehicles
    vehicles = Vehicle.objects.filter(owner=request.user)

    #get vehicle id from post if it exists and retrieve vehicle that matches that id
    vid = request.GET.get('vid')
    display_vehicle = Vehicle.objects.filter(owner=request.user, id=vid)

    return render_to_response('main.html', {
        'vehicles': vehicles,
        'display_vehicle': display_vehicle,
    }, context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "account/register.html", {
        'form': form,
    })

@login_required(login_url='/account/login/')
def add_vehicle(request):
    if request.method == 'POST':
        vehicle = Vehicle(owner=request.user)
        form = VehicleForm(request.POST, instance = vehicle)
        if form.is_valid():
            new_vehicle = form.save()
            return HttpResponseRedirect("/")
    else:
        form = VehicleForm()
    return render(request, "add/addVehicle.html", {
        'form': form,
    })

@login_required(login_url='/account/login/')
def add_history(request):
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            new_history = form.save()
            return HttpResponseRedirect("/")
    else:
        form = HistoryForm()
    return render(request, "add/addHistory.html", {
        'form': form,
    })

@login_required(login_url='/account/login/')
def add_mechanic(request):
    if request.method == 'POST':
        form = MechanicForm(request.POST)
        if form.is_valid():
            new_mechanic = form.save()
            return HttpResponseRedirect("/")
    else:
        form = MechanicForm()
    return render(request, "add/addMechanic.html", {
        'form': form,
    })

@login_required(login_url='/account/login/')
def add_finance(request):
    if request.method == 'POST':
        form = FinanceForm(request.POST)
        if form.is_valid():
            new_finance = form.save()
            return HttpResponseRedirect("/")
    else:
        form = FinanceForm()
    return render(request, "add/addFinance.html", {
        'form': form,
    })

@login_required(login_url='/account/login/')
def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            new_part = form.save()
            return HttpResponseRedirect("/")
    else:
        form = PartForm()
    return render(request, "add/addPart.html", {
        'form': form,
    })
