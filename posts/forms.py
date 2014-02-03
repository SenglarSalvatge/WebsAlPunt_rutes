from django.forms import ModelForm
from posts.models import Post, Dades_Mapa, Categoria
from django.forms.widgets import Textarea
from django import forms
from django.utils.datetime_safe import datetime
from usuaris.models import Perfil

  
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria']
        widgets = {
            'descripcio': Textarea(attrs={'cols': 20, 'rows': 5 }),
        }
        
class CoordenadesForm(ModelForm):
    class Meta:
        model = Dades_Mapa
        fields = ['coordenades']
        
        
class FiltreRutaForm(forms.Form):
    
#initial=datetime.date.today
    
    titol = forms.CharField(max_length=200, required=False)
    data = forms.DateField(required=False)
    dificultat = forms.ChoiceField(choices=Post.DIFICULTAT_CHOICES, required=False)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)
    administrador = forms.ModelChoiceField(queryset=Perfil.objects.filter(postAdministrats__isnull = False).distinct(), required=False)
    