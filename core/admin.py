from django.contrib import admin
from .models import Post, PostVista, Comentarios, Like, User

# Register your models here.
admin.site.register(Post)
admin.site.register(PostVista)
admin.site.register(Comentarios)
admin.site.register(Like)
admin.site.register(User)
