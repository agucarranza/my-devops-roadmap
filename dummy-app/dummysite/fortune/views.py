from django.shortcuts import render
from django.template import loader
from .models import Quote
import datetime
import random

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


def index(request):

    template = loader.get_template('fortune/fortune.html')
    
    all_quotes = [quote.quote_text for quote in Quote.objects.all()]
    random_quote = random.choice(all_quotes)
    context = {
        'random_fortune': random_quote
    }
    return HttpResponse(template.render(context, request))

def add_fortune(request):
   new_fortune_text = request.POST.get('new_fortune', '')  # Obtiene el texto enviado desde el formulario
   # Crea una nueva instancia del modelo Quote con el texto recibido
   new_quote = Quote(quote_text=new_fortune_text, pub_date=datetime.datetime.now())
   # Guarda la nueva cita en la base de datos
   new_quote.save()
   return HttpResponseRedirect('/fortune')