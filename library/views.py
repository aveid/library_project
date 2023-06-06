from django.shortcuts import render, get_object_or_404, redirect

from author.models import Author
from .models import Janr, Book


def get_janrs(request):
    janrs = Janr.objects.all()
    return render(request, "main.html", locals())


def get_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, 'detail_book.html', context)


def create_book(request):
    if request.method == "POST":
        print(request.FILES)
        book_items = {
            "title": request.POST.get("title"),
            "description":request.POST.get("description"),
            "janr": Janr.objects.get(id=int(request.POST.get("janr"))),
            "author": Author.objects.get(id=int(request.POST.get("author"))),
            "publisher": request.POST.get("publisher"),
            "image": request.FILES.get("image"),
            "isdn": request.POST.get("isdn"),
        }
        Book.objects.create(**book_items)
        return redirect("all_janr")
    return render(request=request, template_name="create.html", context=locals())
