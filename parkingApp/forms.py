from django import forms
from .models import Garage, Booking, CustomerReview

from django.forms import ModelForm, HiddenInput



class GarageForm(forms.ModelForm):
    class Meta:
        model = Garage
        exclude = ['lat','lng','rating','ratingCount','avgRating']
        fields = "__all__"

    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['status','totalAmount']
        fields = "__all__" 

class EditForm(forms.ModelForm):
    class Meta:
        model = Garage
        fields = "__all__"
        exclude = ['owner','locality','location','lat','lng']

class BookingStatusForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']


class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = "__all__"
