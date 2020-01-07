from django.shortcuts import render, redirect

from .forms import DonationForm, DonorForm
from .models import Donation

# Create your views here.

def donation_donor_form (request): 
  if request.method == "POST":

    donation_form = DonationForm(request.POST)
    donor_form = DonorForm(request.POST)

    if donation_form.is_valid() and donor_form.is_valid():
      donation = donation_form.save()
      donor = donor_form.save()
      return redirect('/donations')

  else:
    donation_form = DonationForm()
    donor_form = DonorForm()
    
  context = {
    'donation_form': donation_form,
    'donor_form': donor_form
  }

  return render(request, 'donations/donation_donor_form.html', context)



def donation_form_page_view(request, *args, **kwargs):
    return render(request, "donations/donation_form_page.html", {})

def donations_view(request):
  d = Donation.objects.all()
  donations = d[::-1]
  context = {
      "donations": donations
  }
  return render(request, 'donations/donations_view.html', context)


# def get_donation(request):
#   if request.method == 'POST':
#     # create a form instance and populate it with data from the request:
#     form = DonationForm(request.POST)

#     # check whether it's valid:
#     if form.is_valid():
#       form.save()
#       return redirect('/donations')

#       # new_donation = form.save(commit=False)
#       # new_donation.donor_name = request.donor_name
#       # new_donation.email = request.email
#       # new_donation.amount = request.amount
#       # form.save()

#     # if a GET (or any other method) we'll create a blank form
#   else:
#     form = DonationForm()

#   return render(request, 'donations/get_donation.html', {'form': form})
