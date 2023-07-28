from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Yugioh, Buffs, Deck
from django.urls import reverse_lazy
from .forms import BuffsForm 

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

    if request.method == 'POST':
        buffs_form = BuffsForm(request.POST)
        if buffs_form.is_valid():
            buff = buffs_form.save(commit=False)
            buff.yugioh = yugioh_card
            buff.save()
            return redirect('detail', yugioh_card_id=yugioh_card_id)
    else:
        buffs_form = BuffsForm()

    return render(request, 'yugioh/detail.html', {
        'yugioh_card': yugioh_card,
        'buffs_form': buffs_form
    })

class YugiohCreate(CreateView):
  model = Yugioh
  fields = '__all__'

class YugiohUpdate(UpdateView):
  model = Yugioh
  fields = ['type', 'description', 'stars']
  success_url = reverse_lazy('index') 

class YugiohDelete(DeleteView):
    model = Yugioh
    success_url = reverse_lazy('index')

class DeckList(ListView):
  model = Deck

class DeckDetail(DetailView):
  model = Deck

class DeckCreate(CreateView):
  model = Deck
  fields = '__all__'

class DeckUpdate(UpdateView):
  model = Deck
  fields = ['name', 'color']

class DeckDelete(DeleteView):
  model = Deck
  success_url = '/deck'