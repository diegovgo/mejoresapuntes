from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=120)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="careers")

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=120)

class Course(models.Model):
    name = models.CharField(max_length=128)
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="courses")
    subjects = models.ManyToManyField(Subject, related_name="subjects")
    
    def __str__(self):
        return self.name

class MyUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="myuser")
    username = models.CharField(max_length=64, default="0")
    bio = models.CharField(max_length=144, blank=True, null=True)
    university = models.ManyToManyField(University, related_name="myuser")
    career = models.ManyToManyField(Career, related_name="myuser")
    course = models.ManyToManyField(Course, related_name="myuser")
    profile_picture = models.ImageField(upload_to="static/users/profile_picture", blank=True, default="users/profile_picture/nophoto.jpg")
    
    def __str__(self):
        return self.username
 

class File(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=140)
    link = models.CharField(max_length=120, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="documents")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files", default="1", blank=False)
    file = models.FileField(upload_to='users/pdfs', default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=240)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="note")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True, blank=True)
    color = models.CharField(max_length=64, default="#1CBCF9")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", default="1", blank=False)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=120, default="1")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", default="1", blank=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="coments", default="1", blank=False)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="comments", null=True, blank=True )

    def __str__(self):
        return self.text


