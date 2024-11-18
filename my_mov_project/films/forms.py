from models import Film
from django import forms


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                  'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
                  'review': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отзыв'})
                  }