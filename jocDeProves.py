# -*- encoding: utf-8 -*-

def crea_dades():
    

    ###########################################################################################
    #Categories
    ###########################################################################################
    
    from posts.models import Categoria
    
    categories = ['A Peu',
                  'Bicicleta',
                  'Fotting',
                  'Cavall',
                  'Moto',
                  '4x4',
                  ]
    
    for i in categories:
        c = Categoria()
        c.nom = i
        c.save()
        
    ###########################################################################################
    #Posts
    ###########################################################################################
    
    from posts.models import Post
    
    posts = [('Rutes de 4x4 per Palau-Savardera',           #titol
              '2000-02-02',                                 #data
              'Una ruta molt emocionant de 30 segons',      #descripcio
              'EX',                                         #dificultat
              ),
             ('Ruta voladora',
              '2100-02-02',
              'A volar!!!',
              'BA',
              ),
             ('Ruta a peu de Figueres a la China',
              '2791-02-02',
              'La china quin lloc més emocionant, hi ha chinessos i menjar chines',
              'IN',
              ),
             ('Ruta eclesiastica del sagrat cor de Deua',
              '1999-02-02',
              'Rezem germans...',
              'AL',
              ),
             ('Ruta matinera',
              '1800-02-02',
              'Superman!! relleno de pan!',
              'EX',
              ),]
    
    for post in posts:
            p = Post()
            p.titol = post[0]
            p.data = post[1]
            p.descripcio = post[2]
            p.dificultat = post[3]
            p.categoria = Categoria.objects.get(nom='Bicicleta');
            p.administrador = User.objects.get( username = 'manoli').perfil
            p.save()
    
    

        
        
        
        
        
        
        
        
        
        
    

    
