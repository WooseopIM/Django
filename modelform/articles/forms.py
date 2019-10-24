from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         help_text='제목은 20자 이내로 써주세요.',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control my-title',
#                 'placeholder': '제목을 입력해주세요.',
#             }
#         )
#     )
    # content = forms.CharField(
    #     label='내용',
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control my-content',
    #             'placeholder': '내용을 입력해주세요.',
    #             'rows': 5,
    #         }
    #     )
    # )

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
    
    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20자 이내로 써주세요.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-title',
                'placeholder': '제목을 입력해주세요.',
            }
        )
    )
    
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '내용을 입력해주세요.',
                'rows': 5,
            }
        )
    )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)