from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RussianUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=20,
        help_text='Обязательное поле. Не более 20 символов. Только буквы, цифры и символы @/./+/-/_.'
    )
    
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=(
            '<ul>'
            '<li>Ваш пароль не должен быть слишком похож на другую личную информацию.</li>'
            '<li>Ваш пароль должен содержать как минимум 8 символов.</li>'
            '<li>Ваш пароль не может быть часто используемым.</li>'
            '<li>Ваш пароль не может состоять только из цифр.</li>'
            '</ul>'
        ),
    )
    
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='Введите тот же пароль, что и выше, для проверки.',
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок поста'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите содержание поста',
                'rows': 10
            })
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание'
        }