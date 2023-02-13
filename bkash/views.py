from django.shortcuts import render, redirect
from parkingApp.models import Booking

# Create your views here.

def bkashHome(request, id):
    booking = Booking.objects.get(id=id)
    amount = booking.totalAmount
    paymentType = request.POST.get('payment-method')
    if paymentType == "bkash":
        return render(request, 'bkash/bkash_number.html', {'amount':amount, 'tid':id})
    elif paymentType == "cod":
        return render(request, 'bkash/cod.html', {'amount':amount})
    return render(request, 'bkash/bkashHome.html',{'amount':amount})

def bkashNumber(request):	
    return render(request, 'bkash/bkash_number.html')

def bkashPIN(request,id):
    booking = Booking.objects.get(id=id)
    amount = booking.totalAmount
    return render(request, 'bkash/bkash_pin.html', {'amount':amount, 'tid':id})

def bkashSuccess(request,id):
    booking = Booking.objects.get(id=id)
    amount = booking.totalAmount
    return render(request, 'bkash/bkash_success.html')