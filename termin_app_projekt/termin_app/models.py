from django.db import models
from datetime import datetime



"""This class models the appointment object"""
class Appointment(models.Model):
    day = models.DateField("Tag", help_text="Tag des Termins", default=datetime.today())
    start_time = models.TimeField('Beginn', help_text='Beginn des Termins', default=datetime.now())
    end_time = models.TimeField('Ende', help_text='Ende des Termins', default=datetime.now())
    comment = models.CharField("Kommentar", max_length=256, help_text="Freies Kommentar. Gib hier alles ein, was zu diesem Termin wichtig ist.")

    class Meta:
        verbose_name = 'Termin'
        verbose_name_plural = 'Termine'

    def __str__(self):
        return str.format("%s %s-%s Uhr", self.day, self.start_time, self.end_time)