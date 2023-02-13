from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('slotDetail/<id>/', views.slotDetail, name='slotDetail'),
    path('edit/<int:pk>',views.EditView.as_view(), name='editSlot'),
    path('delete/<int:pk>',views.DeleteView.as_view(), name='deleteSlot'),
    path('find_parking/', views.slotSearch, name='slotSearch'),
    path('add_parking/', views.AddParking.as_view(), name='add_parking'),
    path('book_parking/<id>', views.slotBooking, name='book_parking'),
    path('map/', views.mapView, name='map'),
    path('all_bookings/', views.allBookings, name='all_bookings'),
    path('my_bookings/', views.myBooking, name='myBookings'),
    # path('Booking?=accept?/<int:pk>', views.AcceptBooking.as_view(), name='bookingAccept'),
    path('Booking?=accept?/<int:pk>', views.acceptBooking, name='bookingAccept'),
    path('Booking?=reject?/<int:pk>', views.RejectBooking.as_view(), name='bookingReject'),
    # path('Booking?=complete?/<int:pk>', views.CompleteBooking.as_view(), name='bookingComplete'),
    path('Booking?=complete?/<int:pk>', views.completeBooking, name='bookingComplete'),
    path('RentList/', views.myRent, name='RentList'),
    path('rentHistory/', views.rentHistory, name='rentHistory'),
    path('history?=booking/', views.bookingHistory, name='bookingHistory'),
    path('bookings_detail/<id>', views.bookingDetail, name='bookingDetail'),
    path('cancel?=booking/<int:pk>', views.CancelBooking.as_view(), name='cancelBooking'),
    path('my_garage/', views.myGarage, name='myGarage'),
    path('customer_review/<id>', views.customerReview, name='customerReview'),
    path('cancel_review/<int:pk>', views.CancelReview.as_view(), name='cancelReview'),



]