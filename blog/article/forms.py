from django import forms

from .models import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'article_image']

    title =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Title',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))

    content =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Content',
        'class' : 'w-full py-4 px-6 rounded-xl'
    }))
    article_image =  forms.ImageField

    