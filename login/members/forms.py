from django import forms

from .models import booking

class dateinput(forms.DateInput):
    input_type='date'
class bookingform(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'

        widgets={
            'booking_date':dateinput()
        }