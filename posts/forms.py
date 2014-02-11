from django.forms import ModelForm
from posts.models import Post, Dades_Mapa, Categoria
from django import forms
from usuaris.models import Perfil
from django.forms.widgets import Textarea, HiddenInput, DateInput


class PostForm(ModelForm):
    postCoordenades = forms.CharField()
    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria']
        widgets = {
            'descripcio': Textarea(attrs={'cols': 20, 'rows': 5 }),
            'data': DateInput(attrs={'class': 'datepicker'})
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
    



