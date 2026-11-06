from django.contrib import admin
from blog.models import post

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'date_posted','content')

