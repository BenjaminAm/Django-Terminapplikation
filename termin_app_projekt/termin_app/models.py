from django.db import models

"""This class models the appointment object"""
class Appointment(models.Model):
    date_time = models.DateTimeField(help_text="Zeitpunkt des Termins")
    comment = models.CharField(max_length=256, help_text="Freies Kommentar. Gib hier alles ein, was zu diesem Termin wichtig ist.")

    def __str__(self):
        return self.date_time