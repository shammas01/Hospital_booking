from django.contrib import admin
from .models import department,doctor,booking
# Register your models here.
admin.site.register(department)
admin.site.register(doctor)







class BookingAdmin(admin.ModelAdmin):
    list_display =( 'id', 'p_name','p_phone','p_email')

admin.site.register(booking,BookingAdmin)  