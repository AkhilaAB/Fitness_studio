from django.urls import path
from .views import *

urlpatterns = [
    path('classes/', FitnessClassList.as_view(), name='fitness_class_list'),
    path('book/', BookClass.as_view(), name='book_class'),
    path('bookings/', BookingList.as_view(), name='booking_list'),
]