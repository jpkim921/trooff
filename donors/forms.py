from django import forms

from .models import Donor


class DonationForm(forms.ModelForm):

  class Meta:
    model = Donor
    fields = '__all__'
