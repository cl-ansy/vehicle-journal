from django import forms
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from vjournal.apps.vjournal.models import Vehicle


@login_required(login_url='/account/login/')
def index(request):
    #get all the vehicles that belong to the user that is logged in to create
    #a list of vehicles
    vehicles = Vehicle.objects.filter(owner=request.user)

    return render_to_response('main.html', {
        'vehicles': vehicles,
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
