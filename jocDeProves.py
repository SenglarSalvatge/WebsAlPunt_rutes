# -*- encoding: utf-8 -*-

def crea_dades():
    
    ###########################################################################################
    #Usuaris
    ###########################################################################################
    
    from django.contrib.auth.models import User
    users = [('john',
              'john@lennon.com',
              'john',
              ),]
    
    for user in users:
        u = User.objects.create_user(username=user[0], email=user[1], password=user[2])
        u.save()
    ###########################################################################################
    #Categories
    ###########################################################################################
    
    from posts.models import Categoria
    
    categories = ['A Peu',
                  'Bicicleta',
                  '4x4',
                  'Moto',
                  'Fotting',
                  'Cavall',
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
    import time 

    for _ in range(50):
        for post in posts:
                p = Post()
                p.titol = post[0]
                p.data = post[1]
                p.descripcio = post[2]
                p.dificultat = post[3]
                p.categoria = Categoria.objects.get(nom='Bicicleta');
                p.administrador = User.objects.get( username = 'john').perfil
                p.coordenades = '(42.57169583652935, 2.9897403717041016)(42.57125337607666, 3.0066490173339844)(42.56407875783327, 2.9998254776000977)(42.56426840593728, 2.9902124404907227)(42.56787161037666, 2.994546890258789)'
                p.save()
        time.sleep(1)

        
        
        
        
        
        
        
        
        
        
    

    
