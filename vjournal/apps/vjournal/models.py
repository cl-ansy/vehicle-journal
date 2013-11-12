from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user = instance)

post_save.connect(create_user_profile, sender = User)

class Vehicle(models.Model):
    owner = models.ForeignKey('UserProfile')

    make = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    VIN = models.IntegerField()
    license = models.CharField(max_length=8)
    purchase_date = models.DateField()

    additional_info = models.CharField(max_length=60)

    def __unicode__(self):
        return "%d %s %s" % (self.year, self.make, self.model)

class History(models.Model):
    vehicle = models.ForeignKey('Vehicle')

    history_id = models.IntegerField()
    location = models.CharField(max_length=45)
    current_mileage = models.IntegerField()
    maintenance_type = models.CharField(max_length=60)
    date_performed = models.DateField()
    self_maintenance = models.BooleanField(default=False)

    additional_info = models.CharField(max_length=60)

    #build RESTful URLs in the backend -- eventually
    def get_absolute_url(self):
        return 'ZE URL'

    def __unicode__(self):
        return unicode(self.history_id)

class Mechanic(models.Model):
    history = models.ForeignKey('History')

    name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=70)
    specialty = models.CharField(max_length=45)

    def __unicode__(self):
        return self.name

class Finance(models.Model):
    history = models.ForeignKey('History')

    finance_id = models.IntegerField()
    insurance_paid = models.IntegerField()
    date_due = models.DateField()
    date_paid = models.DateField()
    deductible = models.IntegerField()
    insurance_notes = models.CharField(max_length=80)
    repair_cost = models.IntegerField()

    def __unicode__(self):
        return unicode(self.finance_id)

class Part(models.Model):
    history = models.ForeignKey('History')

    name = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    warranty_expiration = models.DateField()
    vendor = models.CharField(max_length=45)
    price = models.IntegerField()

    def __unicode__(self):
        return "%s for history: %s" % (self.name, self.history)
