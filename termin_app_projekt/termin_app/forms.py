from django.forms import Form, ModelForm, SplitDateTimeWidget, CharField, PasswordInput, CheckboxInput
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
            'private': CheckboxInput(),
        }
        fields = ['title', 'start_time', 'end_time', 'comment', 'private']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        #self.fields['start_time'].input_formats = ('%d-%m-%Y %H:%M',)
        #self.fields['end_time'].input_formats = ('%d-%m-%Y %H:%M',)
