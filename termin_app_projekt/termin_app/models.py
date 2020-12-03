from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    """
    Custom user model as recommended by django docs if customization of the user model is needed later.
    """
    pass


class Appointment(models.Model):
    """
    This class models the appointment object
    """
    title = models.CharField('Titel', max_length=50, help_text='Titel des Termins', default='Neuer Termin')
    date = models.DateField('Datum', help_text='Datum des Termins', default=datetime.now)
    start_time = models.TimeField('Beginn', help_text='Beginn des Termins', default=datetime.now)
    end_time = models.TimeField('Ende', help_text='Ende des Termins', default=datetime.now)
    comment = models.CharField('Kommentar', max_length=256, help_text='Freies Kommentar. Gib hier alles ein, was zu diesem Termin wichtig ist.', default='', blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    private = models.BooleanField('Privat', default=True, help_text='Private Termine kannst nur du sehen, andere Termine sehen alle Nutzer.')

    class Meta:
        verbose_name = 'Termin'
        verbose_name_plural = 'Termine'

    def __str__(self):
        return '{0} {1}-{2} Uhr'.format(self.date, self.start_time, self.end_time)

    @property
    def get_html_url(self):
        url = reverse('appointment_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


