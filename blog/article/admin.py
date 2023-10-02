from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'creation_date']
    
    list_display_links = ['title', 'creation_date']
    
    search_fields = ['title']
    
    list_filter = ['creation_date']
    
    prepopulated_fields = {'slug':('title',)} 
    
    class Meta:
        model = Article
