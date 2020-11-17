from django.db import models
from datetime import datetime

from django.urls import reverse

"""This class models the appointment object"""
class Appointment(models.Model):
    title = models.CharField("Titel", max_length=50, help_text="Titel des Termins", null=True)
    start_time = models.DateTimeField('Beginn', help_text='Beginn des Termins', default=datetime.now())
    end_time = models.DateTimeField('Ende', help_text='Ende des Termins', default=datetime.now())
    comment = models.CharField("Kommentar", max_length=256, help_text="Freies Kommentar. Gib hier alles ein, was zu diesem Termin wichtig ist.", null=True)

    class Meta:
        verbose_name = 'Termin'
        verbose_name_plural = 'Termine'

    def __str__(self):
        return str.format("%s %s-%s Uhr", self.day, self.start_time, self.end_time)

    @property
    def get_html_url(self):
        url = reverse('appointment_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'