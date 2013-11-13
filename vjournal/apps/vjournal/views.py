from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from vjournal.apps.vjournal.models import Vehicle


@login_required(login_url='/login/')
def index(request):
    #get all the vehicles that belong to the user that is logged in to create
    #a list of vehicles
    vehicles = Vehicle.objects.filter(owner=request.user)
    print request.user
    return render_to_response('main.html', {
        'vehicles': vehicles,
        }, context_instance=RequestContext(request))


