from django import forms


# class AuthorForm(forms.Form):
#     full_name = forms.CharField(max_length=100)
#     biography = forms.CharField(max_length=200)
from author.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"