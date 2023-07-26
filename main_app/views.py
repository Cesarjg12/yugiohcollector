from django.shortcuts import render
from .models import Yugioh

# Create your views here.
yugioh = [
  {'name': 'Card', 'type': 'monster', 'description': 'A wizard with a staff', 'stars': 7},
  {'name': 'Card2', 'type': 'monster', 'description': 'A black dragon', 'stars': 7},
 
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def yugioh_index(request):
  yugioh = Yugioh.objects.all()
  return render(request, 'yugioh/index.html', {
    'yugioh': yugioh
  })