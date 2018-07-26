from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.template import loader


from .models import Review, MovieToWatch

def index(request):
    reviews = Review.objects.all()
    
    jsonMovieToWatchs = serialize('json', MovieToWatch.objects.all())
    movietowatchs = MovieToWatch.objects.all()
    
    
    template = loader.get_template('life/index.html')
    context = {
      'reviews': reviews,
      'movietowatchs': movietowatchs,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(jasonReviews, content_type="application/json")
    #render(request, 'life/index.html')
    

