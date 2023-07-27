from django.forms import ModelForm
from .models import Buffs

class BuffsForm(ModelForm):
    class Meta:
        model = Buffs
        fields = ['date', 'effect']