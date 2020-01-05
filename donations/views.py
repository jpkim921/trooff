from django.shortcuts import render, redirect

from .forms import DonationForm
from .models import Donation

# Create your views here.

# def donations_made_view(request, *args, **kwargs):
#     # obj = Donation.objects.get(id=1)
#     donations = Donation.objects.all()
#     context = {
#         # 'donor_name': obj.donor_name,
#         # 'email': obj.email,
#         # 'amount': obj.amount,
#         # 'date': obj.date
#         'donations': donations
#     }
#     return render(request, "donations_made_view.html", context)


# Create your views here.

def donation_form_page_view(request, *args, **kwargs):
    return render(request, "donations/donation_form_page.html", {})

def donations_view(request):
  d = Donation.objects.all()
  donations = d[::-1]
  context = {
      "donations": donations
  }
  return render(request, 'donations/donations_view.html', context)


def get_donation(request):
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = DonationForm(request.POST)

    # check whether it's valid:
    if form.is_valid():
      form.save()
      return redirect('/donations')

      # new_donation = form.save(commit=False)
      # new_donation.donor_name = request.donor_name
      # new_donation.email = request.email
      # new_donation.amount = request.amount
      # form.save()

    # if a GET (or any other method) we'll create a blank form
  else:
    form = DonationForm()

  return render(request, 'donations/get_donation.html', {'form': form})
