from django.shortcuts import render, get_object_or_404
from .models import Post,Autor

# Create your views here.
def inicio(request):
    # contexto = {'titulo' : 'Mi primer millon', 'autor': 'Yo'}
    entradas = Post.objects.all()
    contexto = {'entradas': entradas , 'autores': Autor.objects.all()}
    return render(request, 'blog/inicio.html', contexto )
    
def detalle_post(request,pk):
    # entrada = Post.objects.get(pk = pk)
    cont = get_object_or_404(Post,pk=pk)
    # contexto = {'entrada': entrada}
    return render(request, 'blog/detalle_post.html', {'entrada': cont} )


def autor_post(request,pk):
    autor = get_object_or_404(Autor,pk=pk)
    entradas = Post.objects.filter(autor=autor)
    contexto = {'entradita': entradas, 'autor': autor}
    return render(request, 'blog/autor_post.html', contexto )


def autores(request):
    entradas = Autor.objects.all()
    contexto = {'entradita': entradas}
    return render(request, 'blog/autores.html', contexto )



# Post.objects.all()
# Post.objects.filter(titulo__endswith = 'a')
# Post.objects.filter(titulo__startswith = 'M')
# Post.objects.order_by('titulo')
# Post.objects.order_by('titulo').reverse()