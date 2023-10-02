from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Writer")
    title = models.CharField(max_length=200)
    content = RichTextField()
    creation_date = models.DateTimeField(auto_now_add=True,verbose_name="Creation Date")
    article_image = models.FileField(blank=True, null=True, verbose_name="Article Image")
    slug = models.SlugField(unique=True,max_length=100)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Slug(self.title)
        return super(Article, self).save(*args, **kwargs)
