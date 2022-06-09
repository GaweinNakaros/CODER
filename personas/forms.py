
from django import forms


class Alta_Familiar(forms.Form):

    nombre = forms.CharField(max_length=40)    
    edad = forms.IntegerField()            
    
class Alta_Amigos(forms.Form):

    nombre = forms.CharField(max_length=40)    
    edad = forms.IntegerField()

class Alta_Clientes(forms.Form):

    nombre = forms.CharField(max_length=40)    
    edad = forms.IntegerField()      