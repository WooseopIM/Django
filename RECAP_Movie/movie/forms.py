from django import forms
from .models import Movie, Review
from datetime import datetime

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'title_en', 'audience', 'open_date', 'genre', 'watch_grade', 'score', 'poster_url', 'description',)
    title = forms.CharField(
        label='영화제목',
        help_text='영화제목을 적어주세요',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control movie-title',
                'placeholder': '영화제목을 입력해주세요',
            }
        )
    )

    open_date = forms.DateTimeField(
        label='개봉일',
        #widget=forms.DateTimeInput(attrs={'type':'datetime-local'})
        widget=forms.DateTimeInput()
    )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'score',)

    content = forms.CharField(
        label='영화한줄평',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control review_content',
                'placeholder': '영화감상 한줄평을 적어주세요(200자)',
                'row':1,
                'col':50,
            }
        )
    )