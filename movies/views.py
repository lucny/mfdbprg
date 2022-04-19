from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from movies.models import Film, Genre
from movies.forms import FilmModelForm

def index(request):
    context = {
        'num_films': Film.objects.all().count(),
        'films': Film.objects.order_by('-release_date')[:3],
        'top_ten': Film.objects.order_by('-rate')[:10],
        'genres': Genre.objects.order_by('name').all()
    }
    return render(request, 'index.html', context=context)


class FilmListView(ListView):
    model = Film
    context_object_name = 'films'
    template_name = 'film/list.html'

    def get_queryset(self):
        if 'genre_name' in self.kwargs:
            return Film.objects.filter(genres__name=self.kwargs['genre_name']).all()
        else:
            return Film.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_films'] = len(self.get_queryset())
        if 'genre_name' in self.kwargs:
            context['view_title'] = self.kwargs['genre_name']
        else:
            context['view_title'] = 'Filmy'
        return context



class FilmDetailView(DetailView):
    model = Film
    context_object_name = 'film_detail'
    template_name = 'film/detail.html'


class GenreListView(ListView):
    model = Genre
    template_name = 'blocks/genre_list.html'
    context_object_name = 'genres'
    queryset = Genre.objects.order_by('name').all()


class NewFilmListView(ListView):
    model = Film
    template_name = 'blocks/new_films.html'
    context_object_name = 'films'
    queryset = Film.objects.order_by('-release_date').all()


class FilmCreate(CreateView):
   model = Film
   fields = ['title', 'plot', 'release_date', 'runtime', 'poster', 'rate', 'genres']
   initial = {'rate': '5'}


class FilmUpdate(UpdateView):
    model = Film
    template_name = 'movies/film_bootstrap_form.html'
    form_class = FilmModelForm
    #fields = '__all__'