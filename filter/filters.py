import django_filters
from . models import Book
from django import forms

class BookFilters(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    genre = django_filters.MultipleChoiceFilter(choices=Book.GENRE_CHOICES.choices,
                                                widget =forms.CheckboxSelectMultiple()
                                                )
    class Meta:
        model = Book 
        fields = {'name':['icontains'],
                  'author__name':['icontains'],
                  
                }