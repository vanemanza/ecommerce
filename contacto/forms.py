from django import forms
from .models import Contacto

class FormularioContacto(forms.ModelForm):

    nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control"}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Contacto
        fields = "__all__"
    

 