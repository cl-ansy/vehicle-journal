from django.shortcuts import render_to_response
from django.template import RequestContext
from vjournal.apps.vjournal.models import Vehicle


def index(request):
    #get all the vehicles that belong to the user that is logged in to create
    #a list of vehicles
    vehicles = Vehicle.objects.all()

    return render_to_response('main.html', {
        'vehicles': vehicles,
        }, context_instance=RequestContext(request))


