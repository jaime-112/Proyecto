from django.shortcuts import redirect, render, get_object_or_404
from .models import Post,Autor
from .forms import Autorform
from .forms import AutorModelform

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


def autor_editar(request, pk):
    autor = get_object_or_404(Autor,pk=pk)

    if request.method == 'POST':
        form = AutorModelform(request.POST,instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorModelform(instance=autor)
        estado = 'editando'
    contexto = {'form': form, 'estado': estado}
    return render(request, 'blog/autor_nuevo.html', contexto)





def autor_nuevo(request):
    if request.method == 'POST':
        form = AutorModelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorModelform()
        estado = 'creando'
    contexto = {'form': form, 'estado': estado}
    return render(request, 'blog/autor_nuevo.html', contexto)



def autor_borrar(request, pk):
    autor = get_object_or_404(Autor,pk=pk)

    if request.method == 'POST':
        form = AutorModelform(request.POST,instance=autor)
        if form.is_valid():
            autor.delete()
            return redirect('autores')
    else:
        form = AutorModelform(instance=autor)
        estado = 'Borrando'
    contexto = {'form': form, 'estado': estado}
    return render(request, 'blog/autor_nuevo.html', contexto)

