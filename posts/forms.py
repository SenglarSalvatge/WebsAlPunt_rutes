from django.forms import ModelForm
from posts.models import Post, Dades_Mapa
from django import forms
  
class PostForm(ModelForm):
    postCoordenades = forms.CharField()
    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria', 'administrador']
        
class CoordenadesForm():
    class Meta:
        model = Dades_Mapa
        fields = ['coordenades']