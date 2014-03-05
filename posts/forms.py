from django.forms import ModelForm
from posts.models import Post, Categoria
from django import forms
from django.forms.widgets import Textarea, TextInput, Select, HiddenInput, DateInput
from usuaris.models import Perfil


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria', 'coordenades',]
        widgets = {
            'titol': TextInput(attrs={'class':'form-control'}),
            'descripcio': Textarea(attrs={'cols': 20, 'rows': 5, 'class':'form-control'}),
            'dificultat': Select(attrs={'class':'form-control'}),
            'categoria': Select(attrs={'class':'form-control'}),
            'coordenades': HiddenInput(attrs={}),
            'data': DateInput(format='%d/%m/%Y', attrs={'class':'form-control datepicker'}),
        }
        
        
class FiltreRutaForm(forms.Form):
    titol = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'autocomplete':'on', 'class':'form-control'}))
    data = forms.DateField(required=False, widget=DateInput(format='%d/%m/%Y', attrs={'class':'form-control datepicker'}))
    dificultat = forms.ChoiceField(choices=Post.DIFICULTAT_CHOICES ,required=False, widget =  Select(attrs={'class':'form-control'}))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, widget =  Select(attrs={'class':'form-control'}))
    administrador = forms.ModelChoiceField(queryset=Perfil.objects.filter(postAdministrats__isnull = False).distinct(), required=False, widget =  Select(attrs={'class':'form-control'}))