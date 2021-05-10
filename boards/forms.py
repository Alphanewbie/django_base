from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class" : "form-control",
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs= {
                "class" : "form-control",
            }
        )
    )
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ('user',)