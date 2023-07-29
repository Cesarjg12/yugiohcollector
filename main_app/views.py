import os
import uuid
import boto3
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Yugioh, Buffs, Deck, Photo
from django.urls import reverse_lazy, reverse
from .forms import BuffsForm 

# Create your views here.
# yugioh = [
#   {'name': 'Card', 'type': 'monster', 'description': 'A wizard with a staff', 'stars': 7},
#   {'name': 'Card2', 'type': 'monster', 'description': 'A black dragon', 'stars': 7},
 
# ]

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
            return redirect('yugioh_detail', yugioh_card_id=yugioh_card_id)
    else:
        buffs_form = BuffsForm()

    # Get all decks available in the database
    all_decks = Deck.objects.all()

    # Get decks associated with the Yugioh card
    associated_decks = yugioh_card.deck.all()

    # Get available decks (decks not associated with the Yugioh card)
    available_decks = all_decks.exclude(id__in=associated_decks)

    # Get the photos associated with the Yugioh card
    photos = yugioh_card.photo_set.all()

    return render(request, 'yugioh/detail.html', {
        'yugioh_card': yugioh_card,
        'buffs_form': buffs_form,
        'available_decks': available_decks,
        'photos': photos,  # Add the photos to the template context
    })

class YugiohCreate(CreateView):
  model = Yugioh
  fields = ['name', 'type', 'description', 'stars']
  success_url = reverse_lazy('index')

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

def assoc_deck(request, yugioh_card_id, deck_id):
    yugioh_card = get_object_or_404(Yugioh, id=yugioh_card_id)
    deck = get_object_or_404(Deck, id=deck_id)

    yugioh_card.deck.add(deck)
    return redirect('yugioh_detail', yugioh_card_id=yugioh_card_id)

def unassoc_deck(request, yugioh_card_id, deck_id):
    yugioh_card = get_object_or_404(Yugioh, id=yugioh_card_id)
    deck = get_object_or_404(Deck, id=deck_id)

    yugioh_card.deck.remove(deck)
    return redirect('yugioh_detail', yugioh_card_id=yugioh_card_id)


def add_photo(request, yugioh_card_id):
    # photo-file maps to the "name" attr on the <input>
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # Need a unique "key" (filename)
        # It needs to keep the same file extension
        # of the file that was uploaded (.png, .jpeg, etc.)
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # Get the Yugioh object using the provided ID
            yugioh_card = get_object_or_404(Yugioh, id=yugioh_card_id)
            # Create a Photo object associated with the Yugioh card
            print("Photo URL:", url)
            Photo.objects.create(url=url, yugioh=yugioh_card)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('yugioh_detail', yugioh_card_id=yugioh_card_id)