from django.db import models

# Create your models here.
class Yugioh(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    stars = models.IntegerField()


# y = Yugioh(name="Dark Magician", description='The ultimate wizard in terms of attack and defense.', stars=7)

# # Access the dictionary representation of the object
# y_dict = y.__dict__
# print(y_dict)

# Changing this instance method
# does not impact the database, therefore
# no makemigrations is necessary
def __str__(self):
    return f'{self.name} ({self.id})'
