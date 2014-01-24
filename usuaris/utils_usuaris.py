from random import choice
from django.db.models.loading import get_model


def inventat_un_nou_nick():
    nicks1 = [ 'falco', 'tigre', 'drac', 'lleo' ]
    nicks2 = ['groc', 'verd', 'taronjja']
    nicks3 = [ 'milenari','centenari']
    
    Perfil = get_model('usuaris', 'Perfil')
    
    repetit = True
    while repetit:
        proposta = choice( nicks1 ) + ' ' + choice( nicks2 ) + ' ' + choice( nicks3 )
        repetit = Perfil.objects.filter( nick = proposta ).exists()
         
    return  proposta

