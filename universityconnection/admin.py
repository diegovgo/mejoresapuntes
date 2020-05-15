from django.contrib import admin
from .models import University, Course, File, Note, Post, Comment, Subject, Career, MyUser
from import_export.admin import ImportExportModelAdmin

@admin.register(University, Course, File, Note, Post, Comment, Subject, Career, MyUser)
class ViewAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
#admin.site.register(University)
#admin.site.register(Course)
#admin.site.register(Files)