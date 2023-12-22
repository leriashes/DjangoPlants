from django import forms
from .models import Rastenie

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