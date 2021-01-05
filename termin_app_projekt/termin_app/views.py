from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from datetime import date, timedelta
from .forms import LoginForm, AppointmentForm
from django.views.decorators.http import require_http_methods
from .models import *
from .utils import Calendar
from calendar import monthrange
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout


@require_http_methods(["GET", "POST"])
def loginView(request):
    """Login view for StudIP sign in"""
    if request.method == "GET":
        login_data = LoginForm()
        return render(request, "login.html", {'form': login_data})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login')


def logoutView(request):
    logout(request)
    # Redirect to a success page.
    return redirect("/")


class CalendarView(generic.ListView):
    """View to see all allowed appointments in a calendar"""

    model = Appointment
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True, currentuser=self.request.user)
        context['calendar'] = mark_safe(html_cal)

        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def appointment(request, appointment_id=None):
    if appointment_id:
        # if user edits a form
        instance = get_object_or_404(Appointment, pk=appointment_id)
    else:
        # if user creates a new form
        instance = Appointment(owner=request.user)
    form = AppointmentForm(request.POST or None, instance=instance)
    # if user saves the form
    if request.POST and 'save' in request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    # if user presses the delete button
    if request.POST and 'delete' in request.POST:
        if appointment_id:
            Appointment.objects.filter(pk=appointment_id).delete()
            return HttpResponseRedirect(reverse('calendar'))

    return render(request, 'appointment.html', {'form': form})