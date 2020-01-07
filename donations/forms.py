from django import forms

from .models import Donation, Donor


class DonationForm(forms.ModelForm):
  class Meta:
    model = Donation
    fields = [
      'amount'
    ]


class DonorForm(forms.ModelForm):

  class Meta:
    model = Donor
    fields = '__all__'
