from django.shortcuts import render, redirect
from universityconnection.models import University, Course, File, Note, Post, Comment, Subject, Career, MyUser
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NoteForm, CustomUserForm, CreatePostForm, FileForm, MyUserForm
from rest_framework import viewsets
from .serializers import CourseSerializer, FileSerializer, NoteSerializer, MyUserSerializer, UniversitySerializer, CareerSerializer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage

#apis
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

    #if user.is_authenticated:
        #current_user = request.user
        #my_current_user = MyUser.objects.get(user_id=current_user)
        #data["myuser"]= my_current_user 
# Create your views here.
def index(request):

    return render(request, "universityconnection/index.html")

#@login_required
#@permission_required('universityconnection.add_note')

#apuntes
@login_required
def addNote(request):
    current_user = request.user
    mcu = MyUser.objects.get(user_id=current_user)
    courses = mcu.course.all()
    mcupp = mcu.profile_picture
    data = {
        'formfile': FileForm(),
        'profilepicture': mcupp,
        'courses': courses,
    }
    if request.method == "POST":
        formfile = FileForm(request.POST, request.FILES)
        if formfile.is_valid():
                n = formfile.save(commit=False)
                n.user = request.user
                n.save()
                return redirect(to='addnote')

    else:
        current_user = request.user
        files = current_user.files.all()
        data['files'] = files
    return render(request, 'universityconnection/apuntes.html', data)

#def apuntes(request):
    context = {
        "universitys": University.objects.all()
    }
    return render(request, "universityconnection/cursos.html", context)

#courses for each university
@login_required
def mycourses(request):
    current_user = request.user
    mcu = MyUser.objects.get(user_id=current_user)
    mcuc = mcu.course.all()
    mcupp = mcu.profile_picture
    files = []
    for i in range(len(mcuc)):
        course = mcuc[i]
        files_to_add = course.documents.all()
        files.extend(files_to_add)

    context = {
        "courses": mcuc,
        "files": files,
        "profilepicture": mcupp,
    }
    return render(request, "universityconnection/course_select.html", context)

#def cursos(request):
#    university_id = int(request.POST["university_id"])
 #   university = University.objects.get(pk=university_id)
 #   courses = university.courses.all()
  #  context = {
   #     "courses": courses
    #}
   # return render(request, "universityconnection/course_select.html", context)

#def cfeufiles(request):
    course_id = int(request.POST["c_id"])
    course = Course.objects.get(pk=course_id)
    files = course.documents.all()
    notes = course.note.all()
    context = {
        "course": course,
        "files": files,
        "notes": notes,
    }  
    return render(request, "universityconnection/course_select_documents.html", context)

def register(request):
    data = {
        'form': CustomUserForm
        }    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='index')

    return render(request, 'registration/register.html', data)



def foro(request):
    data = {
        'form': CreatePostForm
    }
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.user = request.user
            m.save()
            return redirect(to='foro')

    else:
        posts = Post.objects.all()
        data['posts'] = posts
   
    return render(request, 'universityconnection/foro.html', data)

@login_required
def mysales(request):
    
    return render(request, 'universityconnection/misventas.html')

@login_required
def settings(request):
        user_id = request.user.id
        user = MyUser.objects.get(user=user_id)
        data = { 
            'form': MyUserForm(instance=user)
                }
        if request.method =="POST":
            form = MyUserForm(data=request.POST, files=request.FILES, instance=user)
            if form.is_valid():
                form.save()
                data['mensaje']= "guardado corretamente"
                data['form']= form
                return redirect(to='index')

        return render(request, 'universityconnection/configuracion.html', data )

@login_required
def note(request):
    current_user = request.user
    notes = current_user.notes.all()
    mcu = MyUser.objects.get(user_id=current_user)
    mcuc = mcu.course.all()
    mcupp = mcu.profile_picture

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.user = request.user
            m.save()
            return redirect(to='notes')
    else:
        data = {
        'profilepicture': mcupp,
        'notes': notes,
        'courses': mcuc,
        'form': NoteForm(),
        'color': "red",
        }
        
    return render(request, 'universityconnection/notes.html', data)

def fileview(request, id):
    file = File.objects.get(id=id)
    data = {
        'file': file
    }
    return render(request, 'universityconnection/file.html', data)







