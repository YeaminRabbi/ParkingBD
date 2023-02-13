from django.urls import path
from . import views

urlpatterns = [
    path('<id>/',views.bkashHome, name='bkashHome' ),
    path('number',views.bkashNumber, name='number' ),
    path('pin/<id>',views.bkashPIN, name='pin' ),
    path('success/<id>',views.bkashSuccess, name='bkashSuccess' ),
]
