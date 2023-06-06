from django.shortcuts import render, get_object_or_404
from .models import Janr, Book


def get_janrs(request):
    janrs = Janr.objects.all()
    return render(request, "main.html", locals())


def get_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, 'detail_book.html', context)