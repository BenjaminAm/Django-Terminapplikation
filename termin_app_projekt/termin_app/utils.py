from calendar import LocaleHTMLCalendar

from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Appointment
from django.conf import settings
import locale


class Calendar(LocaleHTMLCalendar):

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__(locale=settings.LANGUAGE_CODE)


    def formatday(self, day, appointments):
        appointments_per_day = appointments.filter(date__day=day)
        d = ''
        for appointment in appointments_per_day:
            visibility = "Öffentlich"
            if appointment.private:
                visibility = "Privat"
            html = format_html("<li class='appointment_link customtooltip'> {} <span class='tooltiptext'>"
                               "Startzeit: {}<br>Endzeit: {}<br>Kommentar: {}<br> Sichtbarkeit: {}</span></li>",
                               appointment.get_html_url, appointment.start_time.strftime('%H:%M'),
                               appointment.end_time.strftime('%H:%M'), appointment.comment, visibility)
            # html = f"<li class='appointment_link customtooltip'> {appointment.get_html_url}"\
            #        + f"<span class='tooltiptext'>Startzeit: {appointment.start_time.strftime('%H:%M')}<br>" \
            #          f"Endzeit: {appointment.end_time.strftime('%H:%M')}<br>" \
            #          f"Kommentar: {appointment.comment}<br>" \
            #          f"Erstellt von: {appointment.owner}<br>" \
            #          f"Sichtbarkeit: {visibility}</span>" + "</li>"
            d += html
        if day != 0:
            return format_html("<td><span class='date'>{}</span><ul> {} </ul></td>", mark_safe(day), mark_safe(d))
        return '<td></td>'

    def formatweek(self, theweek, appointments):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, appointments)
        return format_html('<tr> {} </tr>', mark_safe(week))

    def formatmonth(self, withyear=True, currentuser=None):
        appointments = Appointment.objects.filter(date__year=self.year, date__month=self.month, private=False) |\
                       Appointment.objects.filter(date__year=self.year, date__month=self.month, private=True,
                                                  owner=currentuser)
        calendar = '<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
        try:
            calendar += format_html('{}\n', mark_safe(self.formatmonthname(self.year, self.month, withyear=withyear)))
        except locale.Error:
            self.locale = ("de-de")
        calendar += format_html('{}\n', mark_safe(self.formatweekheader()))
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += format_html('{}\n', self.formatweek(week, appointments))
        return calendar
