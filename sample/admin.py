from django.contrib import admin
from .models import User,UserLogin,DemoDate,Buses,Flights,Tours,VisitingData,TravelsData,SeasonsData,TouristPlaces,Distances

admin.site.register(User)
admin.site.register(UserLogin)
admin.site.register(DemoDate)
admin.site.register(Buses)
admin.site.register(Flights)
admin.site.register(Tours)
admin.site.register(VisitingData)
admin.site.register(TravelsData)
admin.site.register(SeasonsData)
admin.site.register(TouristPlaces)
admin.site.register(Distances)


from .models import FlightBookingDetails

@admin.register(FlightBookingDetails)
class FlightBookingDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'booking_date', 'seats_booked', 'total_fare')  # Removed payment_status
    search_fields = ('user__email', 'flight__flight', 'booking_date')
    list_filter = ()


from .models import BusBookingDetails

class BusBookingDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'bus', 'booking_date')
    search_fields = ('user__email', 'bus__bus_num')
    list_filter = ('booking_date',)

admin.site.register(BusBookingDetails, BusBookingDetailsAdmin)