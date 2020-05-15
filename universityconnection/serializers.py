from rest_framework import serializers
from .models import Course, File, Note, MyUser, University, Career

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id','name']

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id','name', 'university']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name', 'career', 'subjects']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['title', 'description', 'link', 'course', 'user', 'file', 'price']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'note', 'course', 'price', 'user']

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['user', 'bio', 'university', 'career', 'course', 'profile_picture']
