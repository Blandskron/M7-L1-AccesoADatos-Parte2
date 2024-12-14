from django.shortcuts import render
from django.db import connection
from .models import Guest, Room

def available_rooms(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hotel_room WHERE is_available = TRUE")
        rows = cursor.fetchall()

    return render(request, 'rooms.html', {'rooms': rows})

def guest_list(request):
    guests = Guest.objects.raw('SELECT * FROM hotel_guest ORDER BY check_in_date DESC')
    return render(request, 'guests.html', {'guests': guests})
