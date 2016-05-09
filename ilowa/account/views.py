from django.shortcuts import render

# Create your views here.
from .models import Person
from django.views.generic import ListView

class IndexView(ListView):
    template_name = 'account/index.html'
    model = 'Person'
    context_object_name = 'person_list'

    def get_queryset(self):
        queryset = Person.objects.order_by('create_on')
        return queryset
