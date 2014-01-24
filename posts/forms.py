from django import forms
from django.forms import ModelForm
from posts.models import Categoria, Post

class PostForm2(forms.Form):
    DIFICULTAT_CHOICES = (
        ('BA', 'Baix'),
        ('IN', 'Intermig'),
        ('AL', 'Alt'),
        ('EX', 'Extrem'),
    )
    
    titol = forms.CharField()
    data = forms.DateField()
    descripcio = forms.CharField()
    dificultat = forms.CharField()
    categoria = forms.CharField()

    
        
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titol','data','descripcio','dificultat','categoria']