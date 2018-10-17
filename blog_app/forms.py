from django import forms
from .models import BlogModel


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        field = {'blog_title','blog_entry', 'username'}
        order_field = {'blog_title','blog_entry','username'}