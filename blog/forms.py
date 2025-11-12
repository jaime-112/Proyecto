from django import forms

class Autorform(forms.Form):
    nombre = forms.CharField(max_length=30,label='Nombre del autor: ')
    apellido = forms.CharField(max_length=50 ,label='Apellido del autor: ')
    edad= forms.IntegerField(required=False,max_value=120 ,label='Edad del autor: ')
   