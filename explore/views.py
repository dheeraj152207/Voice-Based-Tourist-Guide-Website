from itertools import count
from django.shortcuts import render
from explore.models import Explore, ExplorePlaces
from blog.models import BlogPost
# import pyttsx3
# Create your views here.
def explore(request):
    param = Explore.objects.all()
    context = {'explore':param}
    return render(request, 'explore/page22.html', context)

def explorePlaces(request, country):
    places = BlogPost.objects.all()
    country_name = BlogPost.objects.filter(country = country)
    msg = country_name.first()
    dict_places = {'explorePl':places, 'country1':country_name,'msg':msg}
    return render(request, 'explore/exploreplaces.html', dict_places)

def Contact(request):
    return render(request, 'home/Contact.html')