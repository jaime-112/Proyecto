from django import forms
from .models import Autor

class Autorform(forms.Form):
    nombre = forms.CharField(max_length=30,label='Nombre del autor: ')
    apellido = forms.CharField(max_length=50 ,label='Apellido del autor: ')
    edad= forms.IntegerField(required=False,max_value=120 ,label='Edad del autor: ')
   
class AutorModelform(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'edad']


        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
        }