from django import forms

from .models import Donation, Donor


class DonationForm(forms.ModelForm):
  class Meta:
    model = Donation
    fields = [
      'amount'
    ]
    widgets = {
      'amount': forms.NumberInput(attrs={'class': 'cc'})
    }

class DonorForm(forms.ModelForm):

  class Meta:
    model = Donor
    fields = '__all__'
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'name'}),
      'last_name': forms.TextInput(attrs={'class': 'name'}),
      'email': forms.EmailInput(attrs={'class': 'email'}),
      'phone_number': forms.TextInput(attrs={'class': 'phone_number'}),
      'cc_num': forms.TextInput(attrs={'class': 'cc'}),
      'ccv_num': forms.TextInput(attrs={'class': 'cc'}),
      'cc_expiration': forms.TextInput(attrs={'class': 'cc'})
    }
