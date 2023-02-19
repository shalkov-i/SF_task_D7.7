from django_filters import FilterSet, ModelChoiceFilter

from . import forms
from .models import Post, Author



class PostFilter(FilterSet):
    # author = ModelChoiceFilter(field_name='author__auth__username',
    #     queryset=Author.objects.all().values('auth__username'),
    #     label='Author'
    # )
    #widget = forms.DateInput(attrs={'type': 'date'})
    class Meta:
        model = Post
        fields = {
            'heading': ['icontains'],
            'author__auth__username': ['iexact'],
            'time_in': ['gt'],
        }