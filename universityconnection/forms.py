from django import forms
from django.forms import ModelForm
from .models import Note, Post, File, MyUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(ModelForm):
   
   class Meta:
       model = Note
       fields = ['title', 'note', 'course', 'color']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class CreatePostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','text']

class FileForm(ModelForm):
   class Meta:
       model = File
       fields = ['title', 'link','description','file', 'course', 'price']

class MyUserForm(ModelForm):

   class Meta:
       model = MyUser
       fields = ['bio','university', 'career', 'course', 'profile_picture']
    