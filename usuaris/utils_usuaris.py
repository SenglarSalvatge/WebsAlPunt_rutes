from random import choice
from django.db.models.loading import get_model


def inventat_un_nou_nick():
    nicks1 = [ 'falco', 'tigre', 'drac', 'lleo', 'gat', 'gos', 'rata', 'manati', 'serp', 'cuc', 'ornitorinc']
    nicks2 = ['groc', 'verd', 'taronja', 'blau', 'negre', 'blanc', 'vermell', 'marro', 'gris']
    nicks3 = [ '1','2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    
    Perfil = get_model('usuaris', 'Perfil')
    
    repetit = True
    while repetit:
        proposta = choice( nicks1 ) + ' ' + choice( nicks2 ) + ' ' + choice( nicks3 )
        repetit = Perfil.objects.filter( nick = proposta ).exists()
         
    return  proposta

