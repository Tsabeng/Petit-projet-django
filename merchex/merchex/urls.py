from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/',views.band_list,name='band-list'),
    path('bands/<int:id>/',views.band_detail,name='band-detail'),
    path('listings/',views.listings,name='listing-list'),
    path('listings/<int:id>/',views.listing_detail,name='listing-detail'),
    path('contact-us/',views.contact,name='contact'),
    path('about-us/',views.about,name='about'),
]
