from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . forms import BookNameFilterForm
from . models import Book
from . filters import BookFilters
from django.views.generic.list import ListView
# from filter.serializers import BooKSerializer
# from rest_framework.generics import ListApiViw
# from django_filters.rest_framework import DjangoFilterBackend
 

def index(request):
    book_filters = BookFilters(request.GET,queryset=Book.objects.all())
    # form = BookNameFilterForm()
    form = book_filters.form
    context = {
        "form":form,
        "books":book_filters.qs
    }
    return render(request, 'filter/books.html',context)


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset =  super().get_queryset()
        self.filterset = BookFilters(self.request.GET, queryset=queryset)
        return self.queryset.qs
    
    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
    
# class BookSerializer(ListApiViw):
#     queryset = Book.objects.all()
#     filter_backends = (DjangoFilterBackend,)
#     serializer_class = BookSerializer