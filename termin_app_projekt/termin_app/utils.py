from calendar import LocaleHTMLCalendar
from .models import Appointment
from json import dumps


class Calendar(LocaleHTMLCalendar):

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__(locale="de_DE")

    def formatday(self, day, appointments):
        appointments_per_day = appointments.filter(start_time__day=day)
        d = ''
        for appointment in appointments_per_day:
            html = f"<li class='appointment_link customtooltip'> {appointment.get_html_url}"\
                   + f"<span class='tooltiptext'>Startzeit: {appointment.start_time.strftime('%H:%M')}<br>" \
                     f"Endzeit: {appointment.end_time.strftime('%H:%M')}<br>" \
                     f"Kommentar: {appointment.comment}</span>" + "</li>"
            d += html
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, appointments):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, appointments)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        appointments = Appointment.objects.filter(start_time__year=self.year, start_time__month=self.month)
        calendar = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
        calendar += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        calendar += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += f'{self.formatweek(week, appointments)}\n'
        return calendar