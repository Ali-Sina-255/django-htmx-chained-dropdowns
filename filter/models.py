from django.db import models

# Create your models here.
class Book(models.Model):
    class GENRE_CHOICES (models.TextChoices):
        CRIM = 'C'
        NON_FUNCTION = 'F'
        OTHER = 'O'
        SCI_FI = 'S'

    name = models.CharField(max_length=200)
    price = models.FloatField()
    number_in_stack = models.PositiveSmallIntegerField(default=0)
    genre = models.CharField(choices=GENRE_CHOICES.choices, max_length=2)
    author = models.ForeignKey("author", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    