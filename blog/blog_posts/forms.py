from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'description', 'images')


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Search',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-dark', 'placeholder': 'Search...'})
    )
