from django import forms
from .models import Rastenie
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RastenieForm(forms.ModelForm):
    class Meta:
        model = Rastenie
        fields = ('nazvanie', 'semeystvo', 'gruppi', 'izobrazhenie', 'opisanie', 'temperatura', 'osveshenie', 'poliv', 'udobrenie', 'vlazhnost', 'peresadka', 'razmnozhenie')
        labels = {'nazvanie':'Название', 'semeystvo':'Семейство', 'gruppi':'Группа', 'izobrazhenie':'Изображение', 'opisanie':'Описание', 'temperatura':'Температура', 'osveshenie':'Освещение', 'poliv':'Полив', 'udobrenie':'Удобрение', 'vlazhnost':'Влажность', 'peresadka':'Пересадка', 'razmnozhenie':'Размножение'}
        widgets = {'nazvanie': forms.TextInput(attrs={'class': 'form-control'}),
                    'semeystvo': forms.Select(attrs={'class': 'form-select'}),
                    'gruppi': forms.SelectMultiple(attrs={'class': 'form-select', 'multiple': 'true'}),
                    'izobrazhenie': forms.FileInput(attrs={'class': 'form-control'}),
                    'opisanie': forms.Textarea(attrs={'class': 'form-control'}),
                    'temperatura': forms.Textarea(attrs={'class': 'form-control'}),
                    'osveshenie': forms.Textarea(attrs={'class': 'form-control'}),
                    'poliv': forms.Textarea(attrs={'class': 'form-control'}),
                    'udobrenie': forms.Textarea(attrs={'class': 'form-control'}),
                    'vlazhnost': forms.Textarea(attrs={'class': 'form-control'}),
                    'peresadka': forms.Textarea(attrs={'class': 'form-control'}),
                    'razmnozhenie': forms.Textarea(attrs={'class': 'form-control'})}

class LoginForm(forms.ModelForm):
    login = forms.CharField()
    psswd =  forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=4, max_length=50, help_text="Обязательное поле")
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Имя пользователя занято")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError("Пароли не совпадают")
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя пользователя'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Повторите пароль'})