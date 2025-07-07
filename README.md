# FITNESS STUDIO API(DJANGO)
simple Booking API for a fictional fitness studio using Python-Django.

Scenario:
A fitness studio offers classes like Yoga, Zumba, and HIIT. Clients should be able to view available classes and book a spot.

## Requirements
python 3.8+
django 4.x
Django REST framework

## Setup Instructions

```bash
git clone <repo-url>
cd fitness_studio
python -m venv venv
source venv\scrpts\activate  # venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver  #to run

```

## Load sample data

```bash
python manage.py shell
>>> exec(open("sample_data.py").read())
>>> run()
```

## Api endpoints

#### GET /api/classes
    Returns a list of all upcoming fitness classes (name, date/time, instructor, available slots)
#### POST /api/book/
    Books a class
    example:
    -{
        "class_id":1,
        "client_name":"Akhila",
        "client_email":"akhila@example.com"
    }

#### GET /api/bookings/?email=akhila@example.com
    returns all bookings made by that email

