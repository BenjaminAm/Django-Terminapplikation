from django.forms import Form, ModelForm, DateInput, EmailField, CharField, CheckboxInput
from .models import Appointment


class LoginForm(Form):
    email = EmailField(label="Email", help_text="Bitte gib hier deine RZ Email Adresse ein", max_length=50)
    password = CharField(label="Passwort", help_text="Bitte gib hier dein Passwort ein", max_length=50)


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y %H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%d-%m-%Y %H:%M'),
            'private': CheckboxInput()
        }
        fields = ['title', 'start_time', 'end_time', 'comment', 'private']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%d-%m-%Y %H:%M',)
        self.fields['end_time'].input_formats = ('%d-%m-%Y %H:%M',)
