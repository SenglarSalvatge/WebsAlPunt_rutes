from django.forms import ModelForm
from posts.models import Post, Dades_Mapa
from django import forms
from django.forms.widgets import Textarea, TextInput, Select

class PostForm(ModelForm):
    postCoordenades = forms.CharField()
    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria']
        widgets = {
            'titol': TextInput(attrs={'class':'form-control'}),
            'descripcio': Textarea(attrs={'cols': 20, 'rows': 5, 'class':'form-control'}),
            'dificultat': Select(attrs={'class':'form-control'}),
            'categoria': Select(attrs={'class':'form-control'}),
        }
        
class CoordenadesForm(ModelForm):
    class Meta:
        model = Dades_Mapa
        fields = ['coordenades']
        
        
class FiltreRutaForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titol', 'data', 'dificultat', 'categoria', 'administrador', 'puntuacions']
        