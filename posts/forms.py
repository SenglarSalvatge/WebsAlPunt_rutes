from django.forms import ModelForm
from posts.models import Post, Dades_Mapa
from django.forms.widgets import Textarea

  
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria']
        widgets = {
            'descripcio': Textarea(attrs={'cols': 20, 'rows': 5, 'class':'form-control'}),
        }
        
class CoordenadesForm(ModelForm):
    class Meta:
        model = Dades_Mapa
        fields = ['coordenades']
        
        
class FiltreRutaForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titol', 'data', 'dificultat', 'categoria', 'administrador', 'puntuacions']