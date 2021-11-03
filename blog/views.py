from django.shortcuts import render
from .models import *

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    
    contexto = {'posts': posts}
    
    return render(request, 'blog/blog.html', contexto)

def categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    posts = Post.objects.filter(categorias = categoria)
    contexto = {'categoria': categoria, 'posts': posts}
    return render(request, 'blog/categorias.html', contexto )
