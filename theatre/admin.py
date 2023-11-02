from django.contrib import admin

from theatre.models import (
    Reservation,
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
    Ticket,
)


admin.site.register(Reservation)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Play)
admin.site.register(TheatreHall)
admin.site.register(Performance)
admin.site.register(Ticket)
