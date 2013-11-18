from django.forms import ModelForm
from vjournal.apps.vjournal.models import Vehicle

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner']
