from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band,Listing

from listings.forms import ContactUsForm
from django.core.mail import send_mail

from django.shortcuts import redirect

def band_list (request):
    bands=Band.objects.all()
    return render(request,'listings/band_list.html',{'bands':bands})

def band_detail(request,id):
    band =Band.objects.get(id=id) 
    return render(request,
                  'listings/band_detail.html',
                  {'band':band})
def about(request):
    return render(request,'listings/about.html')

def listings(request):
    all_listings = Listing.objects.all()
    return render(request,'listings/listing_list.html',{'all_listings':all_listings})

def listing_detail(request,id):
    listing=Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing':listing})

def contact(request):
    
    if request.method =='POST':
        form =ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "ananyme"} viaMerchEx Conctact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['delphantsabeng13@gmail.com']
            )
            return redirect('email-sent')

    else:
        form=ContactUsForm()
    return render(request,'listings/contact.html',
                  {'form':form})