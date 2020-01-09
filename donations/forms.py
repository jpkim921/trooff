from django import forms

from .models import Donation, Donor


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'amount'
        ]
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'cc', 'placeholder': 'Donation Amount in USD $'})
        }


class DonorForm(forms.ModelForm):

    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'name','placeholder': 'First'}),
            'last_name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Last'}),
            'email': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'jane_doe@gmail.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'phone_number', 'placeholder': '123-456-7890'}),
            'cc_num': forms.TextInput(attrs={'class': 'cc', 'placeholder': 'Donation Amount in USD $'}),
            'ccv_num': forms.TextInput(attrs={'class': 'cc', 'placeholder': 'CCV'}),
            'cc_expiration': forms.TextInput(attrs={'class': 'cc', 'placeholder': 'MM/YYYY'})
        }
