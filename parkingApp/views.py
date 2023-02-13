from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import *
from .models import Garage, Booking, Division, Locality, CustomerReview, PostalCode




def home(request):
    slots = Garage.objects.all().order_by('-id')
    division = Division.objects.all()
    locality = Locality.objects.all()
    context = { 'slots': slots, 'division': division, 'locality': locality}
    return render(request, 'ParkingBD/index.html', context)


def slotDetail(request, id):
    slot = Garage.objects.get(id=id)
    review = CustomerReview.objects.filter(garage=slot)
    if slot.ratingCount:
        avgRating = slot.rating / slot.ratingCount
    else:
        avgRating = 0
    # reviewer = CustomerReview.objects.filter(garage = slot.id)
    context = { 'slot': slot, 'review': review,  'avgRating': avgRating}
    return render(request, 'ParkingBD/slotDetail.html', context)


class DeleteView(DeleteView):
    model = Garage
    context_object_name = 'slot'
    pk_url_kwarg = 'pk'
    template_name = 'ParkingBD/deleteSlot.html'
    success_message = "Parking lot Deleted Successfully"
    success_url = reverse_lazy('myGarage')


class EditView(UpdateView):
    model = Garage
    form_class = EditForm
    context_object_name = 'slot'
    template_name = 'ParkingBD/editSlot.html'
    pk_url_kwarg = 'pk'
    success_message = "Parking lot Updated Successfully"
    success_url = reverse_lazy('myGarage')


def slotSearch(request):
    division = Division.objects.all()
    locality = Locality.objects.all()
    area = Garage.objects.all()
    searched = 'Search Here...'
    result = []
    Rpostals = []
    relatedResult = []
    if request.method == 'GET':
        search = request.GET.get('area')
        searched = str(search)
        for item in area:
            total = (item.location + " " + item.locality.locality_name + " " + item.locality.division.division_name + " " + item.garage_name).lower()
            search = str(search)
            if search.lower() in total:
                Rpostals.append((item.postalCode))
                result.append(item)
    Rpostals = list(set(Rpostals))
    leftInArea =  list(set(area) - set(result))
    for item in leftInArea:
        if item.postalCode in Rpostals:
            relatedResult.append(item)
    slots = Garage.objects.all().order_by('-id')
    context = { 'division': division, 'locality': locality, 'slots': slots, 'result': result, 'searched': searched, 'relatedResult': relatedResult }
    return render(request, 'ParkingBD/slotSearch.html', context)


class AddParking(CreateView):
    model = Garage
    form_class: GarageForm
    template_name = 'ParkingBD/PostParking.html'
    fields = '__all__'
    success_message = "Parking lot Added Successfully"
    error_message = "Invalid Form"
    success_url = reverse_lazy('myGarage')
    
    def get_context_data(self,*args, **kwargs):
        context = super(AddParking, self).get_context_data(*args,**kwargs)
        context['division'] = Division.objects.all()
        context['city'] = Locality.objects.all().order_by('locality_name')
        context['postal'] = PostalCode.objects.all()
        return context 


# def addParking(request):
#     division = Division.objects.all()
#     city = Locality.objects.all()
#     postal = PostalCode.objects.all()
#     if request.method == 'POST':
#         form = GarageForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Parking lot Added Successfully')
#             return redirect('myGarage')
#         else:
#             messages.error(request, 'Invalid Form')
#             return HttpResponseRedirect(request.path_info)
#     else:
#         form = GarageForm()
#     return render(request, 'ParkingBD/PostParking.html', {'form': form, 'division': division, 'city': city, 'postal': postal})


def mapView(request):
    return render(request, 'ParkingBD/GmapSearch.html')


def slotBooking(request, id):
    form = BookingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking Request Sent')
            ruser = request.user
            rbooking = Booking.objects.filter(customer=ruser).first()
            rid = rbooking.id
            
            
            return redirect('../bookings_detail/{}'.format(rid))
            # return redirect('myBookings')
        else:
            messages.error(request, 'Invalid Form')
            return HttpResponseRedirect(request.path_info)
    context = {"form":form}
    slot = Garage.objects.get(id=id)
    context = { 'slot': slot , 'form': form} 
    return render(request, 'ParkingBD/slotbooking.html', context)


@login_required
def allBookings(request):
    return render(request, 'ParkingBD/allBookings.html')


def bookingDetail(request, id):
    booking = Booking.objects.get(id=id)
    if booking.type_of_booking == "Hour":
        totalAmount = booking.booking_quantity * booking.garage.hourly_cost
    elif booking.type_of_booking == "Day":
        totalAmount = booking.booking_quantity * booking.garage.daily_cost
    elif booking.type_of_booking == "Month":
        totalAmount = booking.booking_quantity * booking.garage.monthly_cost
    booking.totalAmount = totalAmount
    booking.save()
    context = { 'booking': booking, 'totalAmount': totalAmount }
    return render(request, 'ParkingBD/bookingDetail.html', context)


def acceptBooking(request, pk):
    id = pk 
    pk = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            if Booking.objects.get(id=id).vehicle_type == "Car":
                target = Booking.objects.get(id=id).garage
                target.car_slot = Booking.objects.get(id=id).garage.car_slot - 1
                target.save()
            elif Booking.objects.get(id=id).vehicle_type == "Bike":
                target = Booking.objects.get(id=id).garage
                target.bike_slot = Booking.objects.get(id=id).garage.bike_slot - 1
                target.save()
            elif Booking.objects.get(id=id).vehicle_type == "Bicycle":
                target = Booking.objects.get(id=id).garage
                target.bicycle_slot = Booking.objects.get(id=id).garage.bicycle_slot - 1
                target.save()
            messages.success(request, 'Booking Accepted')
            return redirect('RentList')
            
    else:
        form = BookingStatusForm(instance=pk)
   
    return render(request, 'ParkingBD/acceptBooking.html', {'form': form})
    

class RejectBooking(UpdateView):
    model = Booking
    form_class = BookingStatusForm
    context_object_name = 'booking'
    template_name = 'ParkingBD/RejectBooking.html'
    pk_url_kwarg = 'pk'
    success_message = "Booking Rejected"
    success_url = reverse_lazy('RentList')


def completeBooking(request, pk):
    id = pk 
    pk = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=pk)
        if form.is_valid():
            form.save()
            if Booking.objects.get(id=id).vehicle_type == "Car":
                target = Booking.objects.get(id=id).garage
                target.car_slot = Booking.objects.get(id=id).garage.car_slot + 1
                target.save()
            elif Booking.objects.get(id=id).vehicle_type == "Bike":
                target = Booking.objects.get(id=id).garage
                target.bike_slot = Booking.objects.get(id=id).garage.bike_slot + 1
                target.save()
            elif Booking.objects.get(id=id).vehicle_type == "Bicycle":
                target = Booking.objects.get(id=id).garage
                target.bicycle_slot = Booking.objects.get(id=id).garage.bicycle_slot + 1
                target.save()
            messages.success(request, 'Booking has been completed successfully')
            return redirect('RentList')
    else:
        form = BookingStatusForm(instance=pk)
    return render(request, 'ParkingBD/completeBooking.html', {'form': form})


class CancelBooking(UpdateView):
    model = Booking
    form_class = BookingStatusForm
    context_object_name = 'booking'
    template_name = 'ParkingBD/cancelBooking.html'
    pk_url_kwarg = 'pk'
    success_message = "Booking has been cancelled successfully"
    success_url = reverse_lazy('myBookings')


@login_required
def myGarage(request):
    garage = Garage.objects.all().filter(owner = request.user.id).order_by('-id')
    context = { 'garage': garage }
    return render(request, 'ParkingBD/myGarage.html', context)


@login_required
def myRent(request):
    booking = Booking.objects.all().filter(owner = request.user.id )
    bookingStat0 = booking.filter( status = 0 )
    bookingStat1 = booking.filter( status = 1 )
    myRent = bookingStat0 | bookingStat1
    myRent = myRent.order_by('-time')
    context = { 'myRent': myRent }
    return render(request, 'ParkingBD/myRents.html', context)


@login_required
def rentHistory(request):
    booking = Booking.objects.all().filter(owner = request.user.id )
    bookingStat2 = booking.filter( status = 2 )  #rejected
    bookingStat3 = booking.filter( status = 3 )  #completed
    bookingStat7 = booking.filter( status = 7 )
    myRentHistory = bookingStat2 | bookingStat3 | bookingStat7
    myRentHistory = myRentHistory.order_by('-time')
    context = { 'myRentHistory': myRentHistory }
    return render(request, 'ParkingBD/rentHistory.html', context)


@login_required
def myBooking(request):
    booking = Booking.objects.all().filter(customer = request.user.id )
    bookingStat0 = booking.filter( status = 0 ) #pending
    bookingStat1 = booking.filter( status = 1 ) #accepted
    bookingStat3 = booking.filter( status = 3 ) #completed&ReviewPending
    myBooking = bookingStat0 | bookingStat1 | bookingStat3
    myBooking = myBooking.order_by('-time')
    context = { 'myBooking': myBooking }
    return render(request, 'ParkingBD/myBookings.html', context)


@login_required
def bookingHistory(request):
    booking = Booking.objects.all().filter(customer = request.user.id )
    bookingStat2 = booking.filter( status = 2 ) #rejected
    bookingStat7 = booking.filter( status = 7 ) #reveiwed
    bookingStat4 = booking.filter( status = 4 ) #cancelled
    myBookingHistory = bookingStat2 | bookingStat7 | bookingStat4
    myBookingHistory = myBookingHistory.order_by('-time')
    context = { 'myBookingHistory': myBookingHistory }
    return render(request, 'ParkingBD/bookingHistory.html', context)


def customerReview(request, id):
    form = CustomerReviewForm(request.POST or None)
    garage = Booking.objects.get(id=id).garage
    booking = Booking.objects.get(id=id)
    if request.method == "POST":
        rating = request.POST['rating']
        if form.is_valid():
            form.save()
            garage.rating = (int(garage.rating) + int(rating))
            garage.ratingCount = garage.ratingCount + 1
            garage.avgRating = garage.rating / garage.ratingCount
            garage.save()
            booking.status = 7
            booking.save()
            messages.success(request, 'Review Added Successfully')
            to = garage.id
            return redirect('../slotDetail/{}/'.format(to)) #gptChat generation
        else:
            messages.error(request, 'Invalid Form')
            return HttpResponseRedirect(request.path_info)
    context = {"form":form}
    slot = garage
    context = { 'slot': slot , 'form': form} 
    return render(request, 'ParkingBD/customerReview.html', context)


class CancelReview(UpdateView):
    model = Booking
    form_class = BookingStatusForm
    context_object_name = 'booking'
    template_name = 'ParkingBD/cancelReview.html'
    pk_url_kwarg = 'pk'
    success_message = "Review done successfully"
    success_url = reverse_lazy('myBookings')