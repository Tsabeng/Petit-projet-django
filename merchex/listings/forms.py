from django import forms 
from listings.models import Band,Listing

class ContactUsForm(forms.Form):
    name=forms.CharField(required=False)
    email=forms.EmailField()
    message=forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model=Band
        exclude =('active','official_homepage') # utiliser exclude signifie que l'utilisateur  aurait les champ du formulaire sauf active et official_homepage ils pourront seulement etre modifier par l'administrateur
       # fields='__all__' # mettre ca signifie que l'on prend tout les champs du models
class ListingForm(forms.ModelForm):

    class Meta:
        model=Listing
        exclude = ('sold',)
        #fields='__all__'