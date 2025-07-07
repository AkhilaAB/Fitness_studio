from studio.models import FitnessClass
from django.utils import timezone
from datetime import timedelta

def run():
    print("Creating sample data...")

    FitnessClass.objects.all().delete()

    FitnessClass.objects.create(
        name="Yoga",
        date_time=timezone.now() + timedelta(days=1, hours=9),
        instructor="Alice Smith",
        total_slots=20,
        available_slots=20
    )
    FitnessClass.objects.create(
        name="Zumba",
        date_time=timezone.now() + timedelta(days=1, hours=10),
        instructor="Rahul Kumar",
        total_slots=15,
        available_slots=15
    )
    FitnessClass.objects.create(
        name="HIIT",
        date_time=timezone.now() + timedelta(days=1, hours=8),
        instructor="Anjali Verma",
        total_slots=10,
        available_slots=10
    )