from django.db import models
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 1 or value > 10000:
        raise ValidationError('La valoración debe estar entre 1 y 10000.')

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)  # Aquí se declara correctamente el campo author
    rating = models.IntegerField(validators=[validate_rating])

    def __str__(self):
        return self.title

# Create your models here.
