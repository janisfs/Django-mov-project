from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from .models import Film



# Create your views here.
def films(request):
    films = Film.objects.all()
    return render(request, 'my_mov_project/films.html', {'films': films})


def add_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form, 'errors': error})



def films_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return render(request, 'films/film_detail.html', {'film': film})