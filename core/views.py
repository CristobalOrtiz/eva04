from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post , PostVista, Comentarios, Like
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    
class PostDetailView(DetailView):
    model = Post
    
    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        print('xd')
        if form.is_valid():
            post = self.get_object()
            comentarios = form.instance
            comentarios.user = self.request.user
            comentarios.post = post
            comentarios.save()
            return redirect('detail', slug=post.slug)
        else:
            context = 'f'
            return HttpResponse(context)
        
    def get_contenido_data(self, **kwargs):
        contenido = super().get_contenido_data(**kwargs)
        contenido.update({
            'form': CommentForm()
        }) 
        return contenido   
    
    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostVista.objects.get_or_create(user=self.request.user, post=object)
        return object
    
class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Crear'
        })
        return context
    
class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Actualizar'
        })
        return context
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    

def Index(request):
    return render(request, 'index.html')

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)

