from django.test import TestCase

from .models import Review, MovieToWatch
from django.core.serializers import serialize
#from django.core import serializers
#from django.http import JsonResponse
#import json

def reviews(request):
  response = serialize('json', Review.objects.all())
  return HttpResponse(response, content_type="application/json")
# Create your tests here.
