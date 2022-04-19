from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Film


class FilmModelForm(ModelForm):
    def clean_runtime(self):
       data = self.cleaned_data['runtime']
       if data <= 0 or data > 1000:
           raise ValidationError('Neplatná délka filmu')
       return data

    class Meta:
        model = Film
        fields = ['title', 'plot', 'release_date', 'runtime', 'poster', 'rate', 'genres']
        labels = {'title': 'Název filmu', 'plot': 'Stručný děj'}