from django.shortcuts import render
from django.template import loader
from .models import Quote
import datetime
import random
import boto3
from uuid import uuid4
from boto3.dynamodb.conditions import Key

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect


def index(request):

    template = loader.get_template('fortune/fortune.html')
    
    all_quotes = [quote.quote_text for quote in Quote.objects.all()]
    random_quote = random.choice(all_quotes)
    random_quote = get_data_from_dynamodb(table_name='fortune', partition_key=1)
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

   save_data_to_dynamodb(partition_key=1, table_name='fortune', data=new_fortune_text)

   return HttpResponseRedirect('/fortune')

def get_data_from_dynamodb(table_name, partition_key):

    # Reference the existing table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)


    # Obtengo valor para entrar a la tabla
    random_value = str(uuid4())
    print(random_value)

    # Buscar un valor unico mayor al random value

    data = table.query(
        Limit=1,
        KeyConditionExpression = 
            Key('id').eq(partition_key) &
            Key('uuid').gte(random_value)
    )

    # Si no encuentro, busco uno menor

    if not data['Items']:
        data = table.query(
        Limit=1,
        KeyConditionExpression = 
            Key('id').eq(partition_key) &
            Key('uuid').lt(random_value)
    )
    
    return data['Items'][0]['cita'] 

def save_data_to_dynamodb(table_name, partition_key, data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    new_uuid = str(uuid4())

    ret = table.put_item(
        Item={
            'id': partition_key,
            'uuid': new_uuid,
            'cita': data
        }
    )
    return ret