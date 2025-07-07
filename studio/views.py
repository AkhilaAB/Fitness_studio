from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking, User
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils.timezone import localtime



class FitnessClassList(APIView):
    def get(self, request):
        fitness_classes = FitnessClass.objects.filter(available_slots__gt=0).order_by('date_time')
        if not fitness_classes:
            return Response({"message": "No available fitness classes found."}, status=status.HTTP_404_NOT_FOUND)
        for class_obj in fitness_classes:
            class_obj.date_time = localtime(class_obj.date_time)
        serializer = FitnessClassSerializer(fitness_classes, many=True)
        return Response(serializer.data)

class BookClass(APIView):
    def post(self, request):
        class_id = request.data.get('class_id')
        email=request.data.get('client_email')
        name=request.data.get('client_name')
        if not all([class_id, email, name]):
            return Response({"error": "class_id, client_email, and client_name are required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            fitness_class = FitnessClass.objects.get(id=class_id)
        except FitnessClass.DoesNotExist:
            return Response({"error": "Fitness class not found."}, status=status.HTTP_404_NOT_FOUND)
        if fitness_class.available_slots <= 0:
            return Response({"error": "No available slots for this class."}, status=status.HTTP_400_BAD_REQUEST)
        user,_= User.objects.get_or_create(
            email=email,
            name=name,username=email
        )
        if Booking.objects.filter(user=user, fitness_class=fitness_class).exists():
            return Response({"error": "You have already booked this class."}, status=status.HTTP_400_BAD_REQUEST)
        booking = Booking.objects.create(user=user, fitness_class=fitness_class)
        fitness_class.available_slots -= 1
        fitness_class.save()
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class BookingList(APIView):
    def get(self, request):
        email=request.GET.get("email")
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
        user= User.objects.filter(email=email).first()
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        bookings = Booking.objects.filter(user=user).order_by('-booking_date')
        if not bookings:
            return Response({"message": "No bookings found for this user."}, status=status.HTTP_404_NOT_FOUND)  
        for booking in bookings:
            booking.fitness_class.date_time = localtime(booking.fitness_class.date_time)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)