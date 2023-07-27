from django.db import models

from django.urls import reverse

EFFECTS = (
  ('M', 'Monster'),
  ('S', 'Spell'),
  ('T', 'Trap'),
)

# Create your models here.
class Yugioh(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    stars = models.IntegerField()

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
def __str__(self):
    return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'cat_id': self.id})

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