from django.contrib import admin
from .models import Yugioh,Buffs, Deck, Photo

# Register your models here.
admin.site.register(Yugioh)
admin.site.register(Buffs)
admin.site.register(Deck)
admin.site.register(Photo)