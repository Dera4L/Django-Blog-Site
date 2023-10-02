from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_date']
    
    list_display_links = ['title', 'created_date']
    
    search_fields = ['title']
    
    list_filter = ['created_date']
    
    prepopulated_fields = {'slug':('title',)}