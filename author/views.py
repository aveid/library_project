from django.shortcuts import render, redirect
from django.views import View

from author.forms import AuthorForm
from author.models import Author


class AuthorView(View):
    model = Author
    template_name = "author.html"
    form_class = AuthorForm

    def get(self, request):
        form = self.form_class()
        authors = self.model.objects.all()
        return render(request, self.template_name, locals())

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         data = {"full_name": request.POST.get("full_name"),
    #                 "biography": request.POST.get("biography"),}
    #         self.model.objects.create(**data)
    #         return redirect('author')
    #     return render(request, self.template_name, locals())
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author')
        return render(request, self.template_name, locals())


class DetailUpdateView(View):
    model = Author
    template_name = "update.html"
    form_class = AuthorForm

    def get(self, request, pk):
        author = self.model.objects.get(id=pk)
        form = self.form_class(instance=author)
        return render(request, self.template_name, locals())

    def post(self, request, pk):
        author = self.model.objects.get(id=pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            author.full_name = request.POST.get("full_name")
            author.biography = request.POST.get("biography")
            author.save()
            return redirect('author')
        return render(request, self.template_name, locals())