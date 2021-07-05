from django import forms
from .models import Post, Comentarios


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('contenido',)