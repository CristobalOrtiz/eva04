from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    thumbnail = models.ImageField()
    fechaP = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'slug': self.slug
        })
        
    def get_like_url(self):
        return reverse('like', kwargs={
            'slug': self.slug
        })
        
    @property
    def come(self):
        return self.comentarios_set.all()
        
    @property
    def get_comment_count(self):
        return self.comentarios_set.all().count()
    
    @property
    def get_view_count(self):
        return self.postvista_set.all().count()
    
    @property
    def get_like_count(self):
        return self.like_set.all().count()
    
class Comentarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class PostVista(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
