from django.forms import ModelForm
from posts.models import Post
from django import forms
from django.forms.widgets import Textarea, HiddenInput

class PostForm(ModelForm):
    postCoordenades = forms.CharField()
    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria', 'coordenades']
        widgets = {
            'descripcio': Textarea(attrs={'cols': 20, 'rows': 5, 'class':'form-control'}),
        }
        
        
class FiltreRutaForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titol', 'data', 'dificultat', 'categoria', 'administrador', 'puntuacions']
