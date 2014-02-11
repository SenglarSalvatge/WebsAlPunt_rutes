from django.forms import ModelForm
from posts.models import Post, Dades_Mapa, Categoria
from django import forms
from django.forms.widgets import Textarea, TextInput, Select, HiddenInput
from usuaris.models import Perfil

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
        widgets = {
                   'coordenades':HiddenInput
                   }
        fields = ['coordenades']
        
class FiltreRutaForm(forms.Form):
    titol = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'autocomplete':'on'}))
    data = forms.DateField(required=False)
    dificultat = forms.ChoiceField(choices=Post.DIFICULTAT_CHOICES ,required=False)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False)
    administrador = forms.ModelChoiceField(queryset=Perfil.objects.filter(postAdministrats__isnull = False).distinct(), required=False)
