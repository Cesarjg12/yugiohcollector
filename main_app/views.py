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

def yugioh_detail(request, yugioh_card_id):
    try:
        yugioh_card = Yugioh.objects.get(id=yugioh_card_id)
    except Yugioh.DoesNotExist:
        return render(request, 'yugioh/detail.html', {'error_message': 'Card does not exist.'})
    
    return render(request, 'yugioh/detail.html', {
        'yugioh_card': yugioh_card
    })