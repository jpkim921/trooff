"""troof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# from pages.views import home_page_view, contact_page_view
# from donations.views import donations_view, donation_form_page_view, donation_donor_form

# urlpatterns = [
#     path('', include('products.urls')),
#     path('', home_page_view),
#     path('donations/', donations_view),
#     # path('donated/', donation_form_page_view),
#     path('donate/', donation_donor_form),
#     path('contact/', contact_page_view),
#     path('admin/', admin.site.urls),
# ]


urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('products.urls')),
    path('admin/', admin.site.urls),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)