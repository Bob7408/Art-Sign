from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from Art_Sign.agenda.forms import EventForm
from Art_Sign.agenda.models import Event


class EventListView(ListView):

    model = Event


class EventCreate(CreateView):
    model = Event
    template_name = 'agenda/new.html'
    form_class = EventForm


