"""
Создание формы
"""

from django import forms

from .models import CD, GENRE_CHOICES


class ExchangeForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    email = forms.EmailField(label='Почта')
    title = forms.CharField(max_length=100, label='Название альбома')
    artist = forms.CharField(max_length=40, label='Исполнитель')
    genre = forms.ChoiceField(choices=GENRE_CHOICES, label='Жанр')
    price = forms.DecimalField(max_digits=5, decimal_places=2, required=False,
                               label='Стоимость')
    comment = forms.CharField(widget=forms.Textarea, required=False,
                                                          label='Комментарий')

    def clean_artist(self):
        artist_change = self.cleaned_data['artist']

        if not CD.objects.filter(artist__icontains=artist_change).exists():
            raise forms.ValidationError('Артиста не существует')

        return artist_change