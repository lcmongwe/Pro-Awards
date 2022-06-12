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
        fields=('image', 'img_name', 'img_url', 'img_description', 'poster'   )

        labels={
            'img_name':'name',
            'img_description':'description',     
        }

        widgets={
           'img_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'  name '}),
           'img_description':forms.TextInput(attrs={'class': 'form-control','placeholder':'description'}),
           'img_url':forms.URLInput(attrs={'class': 'form-control','placeholder':'enter url'}),

        }


class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        # fields= "__all__"
        fields=('name', 'email', 'phone','bio', 'image'  )

        labels={
            'name':'name',
            'email':'email',  
            'phone':'phone',
            'bio':'bio', 
            'image':'image',   

        }

        widgets={
           'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'  name '}),
           'phone': forms.TextInput(attrs={'class': 'form-control','placeholder':'  phone '}),          
           'email':forms.TextInput(attrs={'class': 'form-control','placeholder':'email'}),
           'bio':forms.Textarea(attrs={'class': 'form-control','placeholder':'bio'}),

        }


class ReviewForm(ModelForm):
    class Meta:
        model= Review
        # fields= "__all__"
        fields=('design', 'usability', 'content' )

        labels={
            'design':'design',
            'usability':'usability',
            'content':'content',  
        }

