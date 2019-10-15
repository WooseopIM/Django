from django import forms
from .models import Article, Comment

# class Article(models.Model)
# class ArticleForm(forms.Form):



# 현재 모델폼이 갖고 있는 정보를 Meta 클래스에 정의
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

        # exclude = ('title',) title에 대해서는 Form을 만들지 않는다.
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'placeholder': "제목을 입력해주셈",
        #         'class': 'form-control title-class',
        #         'id': 'title',
        #     })
        # }

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
    
    comment = forms.CharField(
        label='댓글',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control comments',
                'placeholder': '댓글을 입력해주세요',
                'rows': 2,
                'cols': 50,
            }
        ),
    )

