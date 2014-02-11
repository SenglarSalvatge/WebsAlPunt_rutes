#Formulari per poder modificar el perfil d'un usuari
from django.forms import ModelForm
from usuaris.models import Perfil
from django.forms.widgets import Textarea

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        widgets = {
                  'descripcio': Textarea(attrs={'cols':20, 'rows':5 })
                  }
        fields = ['descripcio','nick']