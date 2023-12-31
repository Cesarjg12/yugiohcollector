from django.db import models
from django.urls import reverse
from datetime import date

EFFECTS = (
  ('M', 'Monster'),
  ('S', 'Spell'),
  ('T', 'Trap'),
)
class Deck(models.Model):
   name = models.CharField(max_length=50)
   color = models.CharField(max_length=20)

   def __str__(self):
    return self.name
   
   def get_absolute_url(self):
    return reverse('deck_detail', kwargs={'pk': self.id})
   
# Create your models here.
class Yugioh(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    stars = models.IntegerField()
    deck = models.ManyToManyField(Deck)

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
def __str__(self):
    return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'pk': self.id})

class Buffs(models.Model):
  date = models.DateField()
  effect = models.CharField(
    max_length=1,
    choices=EFFECTS,
    default=EFFECTS[0][0]
  )
  # Create a yugioh_id FK
  yugioh = models.ForeignKey(
    Yugioh,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_effect_display()} on {self.date}"
  
class Meta:
    ordering = ['-date']


class Photo(models.Model):
  url = models.CharField(max_length=200)
  yugioh = models.ForeignKey(Yugioh, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for cat_id: {self.yugioh_id} @{self.url}"