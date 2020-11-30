from django.forms import Form, ModelForm, TimeInput, DateInput, CharField, PasswordInput, CheckboxInput
from .models import Appointment
from datetime import datetime



class LoginForm(Form):
    username = CharField(label="Benutzername", help_text="Bitte gib hier deinen RZ Benutzernamen ein", max_length=50)
    password = CharField(widget=PasswordInput, label="Passwort", help_text="Bitte gib hier dein Passwort ein", max_length=50)


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
            'start_time': TimeInput(attrs={'type': 'time'}),
            'end_time': TimeInput(attrs={'type': 'time'}),
            'private': CheckboxInput(),
        }
        fields = ['title', 'date', 'start_time', 'end_time', 'comment', 'private']
