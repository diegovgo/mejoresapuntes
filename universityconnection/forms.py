from django import forms
from django.forms import ModelForm
from .models import Note, Post, File, MyUser, Filecomment, Commentocomment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NoteForm(ModelForm):
   
   class Meta:
       model = Note
       fields = ['title', 'note', 'course', 'color']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

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
    
class FilecommentForm(ModelForm):
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "rows":2,
                "cols":50,
                "placeholder":"Ingresa tu comentario aquí..."
            }
        )
    )
    class Meta:
        model = Filecomment
        fields = ['comment']

class CommentocommentForm(ModelForm):
  
    class Meta:
        model = Commentocomment
        fields = ['response']

