from django.forms import Form, ModelForm, SplitDateTimeWidget, CharField, PasswordInput
from .models import Appointment


class LoginForm(Form):
    username = CharField(label="Benutzername", help_text="Bitte gib hier deinen RZ Benutzernamen ein", max_length=50)
    password = CharField(widget=PasswordInput, label="Passwort", help_text="Bitte gib hier dein Passwort ein", max_length=50)


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': SplitDateTimeWidget(time_attrs={'type': 'datetime-local'}, time_format='%H:%M',
                                              date_attrs={'type': 'datetime-local'}, date_format='%d.%m.%y%y'),
            'end_time': SplitDateTimeWidget(time_attrs={'type': 'datetime-local'}, time_format='%H:%M',
                                            date_attrs={'type': 'datetime-local'}, date_format='%d.%m.%y%y'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)