from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from django.forms import ModelForm
from .models import Profile,Post,Review

# CREATE POST FORM
class CreatePostForm(ModelForm):
    class Meta:
        model= Post
        # fields= "__all__"
        fields=('image', 'img_name', 'img_url', 'img_description',    )

        labels={
            'img_name':'name',
            'img_description':'description',     
        }

        widgets={
           'img_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'  name '}),
           'img_description':forms.TextInput(attrs={'class': 'form-control','placeholder':'description'}),
           'img_url':forms.TextInput(attrs={'class': 'form-control','placeholder':'enter url'}),

        }