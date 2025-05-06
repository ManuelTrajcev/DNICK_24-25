from django import forms

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_2.settings')
django.setup()

from flight2.models import Flight_2


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):    #nema da pomine bez ovie args
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class FlightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):    #nema da pomine bez ovie args
        super(FlightForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Flight_2
        fields = '__all__'
