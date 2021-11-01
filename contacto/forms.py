from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre", required = True)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    
 