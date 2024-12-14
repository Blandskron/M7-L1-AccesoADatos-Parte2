# Proyecto Django para un Sistema de Gestión de Hoteles

Este proyecto está diseñado para demostrar cómo usar Django para desarrollar un sistema de gestión de hoteles. Se incluye la configuración de bases de datos, creación de modelos para huéspedes y habitaciones, y ejemplos de consultas SQL utilizando el ORM de Django y consultas personalizadas. Este proyecto es educativo y puede servir como base para aplicaciones más avanzadas.

## Tecnologías utilizadas

- **Django**: Framework web en Python.
- **SQLite**: Base de datos por defecto.
- **PostgreSQL**: Base de datos relacional avanzada (opcional).
- **MongoDB**: Base de datos NoSQL (opcional).

## Configuración inicial

1. **Crear el proyecto Django**

   Ejecuta los siguientes comandos en tu terminal para iniciar un proyecto Django:
   ```bash
   django-admin startproject hotel_management
   cd hotel_management
   python manage.py startapp hotel
   ```

2. **Configurar la base de datos**

   En el archivo `hotel_management/settings.py`, agrega la configuración de la base de datos. Por defecto, se utiliza SQLite:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': 'hotel_db',
       }
   }
   ```

   Si prefieres PostgreSQL, usa esta configuración:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'hotel_db',
           'USER': 'postgres',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Soporte para MongoDB (Opcional)**

   Para trabajar con MongoDB, instala el paquete `djongo`:
   ```bash
   pip install djongo
   ```

   Configura `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': 'hotel_db',
       }
   }
   ```

## Crear los modelos

Define los modelos en el archivo `hotel/models.py`:
```python
from django.db import models

class Guest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Room(models.Model):
    ROOM_TYPES = [
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('SUITE', 'Suite'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.get_room_type_display()})"
```

Ejecuta las migraciones para aplicar estos cambios a la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Crear vistas para consultas SQL

En el archivo `hotel/views.py`, crea vistas para ejecutar consultas SQL personalizadas:
```python
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
```

## Configurar URLs

En el archivo `hotel_management/urls.py`, registra las rutas para las vistas:
```python
from django.contrib import admin
from django.urls import path
from hotel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('available-rooms/', views.available_rooms, name='available_rooms'),
    path('guest-list/', views.guest_list, name='guest_list'),
]
```

## Crear plantillas HTML

En la carpeta `hotel/templates/`, crea archivos para mostrar los resultados.

**rooms.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Available Rooms</title>
</head>
<body>
    <h1>Available Rooms</h1>
    <ul>
        {% for room in rooms %}
            <li>Room {{ room.1 }}: {{ room.2 }} - ${{ room.3 }} per night</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**guests.html**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Guest List</title>
</head>
<body>
    <h1>Guest List</h1>
    <ul>
        {% for guest in guests %}
            <li>{{ guest.first_name }} {{ guest.last_name }} ({{ guest.email }})</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Ejecutar el servidor

Para iniciar el servidor y probar las rutas configuradas:
```bash
python manage.py runserver
```

Accede a las rutas configuradas en tu navegador:
- [http://localhost:8000/available-rooms/](http://localhost:8000/available-rooms/): Para ver habitaciones disponibles.
- [http://localhost:8000/guest-list/](http://localhost:8000/guest-list/): Para ver la lista de huéspedes.

## Conclusión

Este proyecto demuestra:
1. Configuración de bases de datos en Django (SQLite, PostgreSQL y MongoDB).
2. Creación de modelos para un sistema hotelero.
3. Consultas SQL personalizadas y manejo de datos utilizando Django.

Es un punto de partida ideal para sistemas de gestión hotelera más complejos.

