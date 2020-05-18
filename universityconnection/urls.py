from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cursos', views.CourseViewSet)
router.register('files', views.FileViewSet)
router.register('notas', views.NoteViewSet)
router.register('myuser', views.MyUserViewSet)
router.register('university', views.UniversityViewSet)
router.register('career', views.CareerViewSet)

urlpatterns = [
    path("misarchivos", views.addNote, name="addnote"),
    path("", views.index, name="index"),
    path("cursos", views.mycourses, name="mycourses"),
    path("register", views.register, name="register"),
    path("foro", views.foro, name="foro"),
    path('api/', include(router.urls)),
    path('misventas/', views.mysales, name="misventas"),
    path('configuracion/', views.settings, name="configuracion"),
    path('notas', views.note, name="notes"),
    path('file/<id>/', views.fileview, name="file"),
    path('registration', views.registrationsteptwo, name="registration_step_2"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
