from django.forms import ModelForm
from socials.models import Comentari
from django.forms.widgets import Textarea

class ComentariForm(ModelForm):
    class Meta:
        model = Comentari
        widgets = {
                   'comentari': Textarea(attrs={'cols':25, 'rows':5 })
                   }
        fields = ['comentari']