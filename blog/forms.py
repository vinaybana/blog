from django import forms

from .models import Post, Category
#from taggit.models import Tag

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class categoryForm(forms.ModelForm):

    class Meta:
    	model = Category
    	fields=('title' , 'text')

