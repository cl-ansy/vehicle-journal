from django.forms import ModelForm
from vjournal.apps.vjournal.models import Vehicle
from vjournal.apps.vjournal.models import Part
from vjournal.apps.vjournal.models import Mechanic
from vjournal.apps.vjournal.models import History
from vjournal.apps.vjournal.models import Finance

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        exclude = ['owner']

class HistoryForm(ModelForm):
	class Meta:
		model = History

class PartForm(ModelForm):
	class Meta:
		model = Part

class MechanicForm(ModelForm):
	class Meta:
		model = Mechanic

class FinanceForm(ModelForm):
	class Meta:
		model = Finance

