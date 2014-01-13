###########################################################################################
#Categories
###########################################################################################

from posts.models import Categoria

categories = list('A Peu',
                  'Bicicleta',
                  '4x4',
                  'Avioneta',
                  'Cabra mecànica',
                  )

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
        p.save()

###########################################################################################
#Usuaris
###########################################################################################

from django.contrib.auth.models import User

users = [('john',
          'john@lennon.com',
          'john',
          ),
         ('pere',
          'pere@peret.net',
          'pere',
          ),
         ('manoli'
          'destruccioninfernal@hotmail.es',
          'manoli',
          ),
         ('elpicdesallafort',
          None,
          'elpicadesallafort'),
         ('william',
          'w12@gmail.com',
          'william'),]

for user in users:
    u = User.objects.create_user(user[0], user[1], user[2])
    u.save()


###########################################################################################
#Perfils
###########################################################################################

###########################################################################################
#Comentaris
###########################################################################################

###########################################################################################
#Puntuacions
###########################################################################################
    
from usuaris.models import Perfil

perfiles = [('Hola me llamo Josele', '1'),
               ('Soy manoli','2'),
               ('Lo peta floreta','3'),
               ('Alex se soba en HTTP y jmeter','4'),
               ('Jodido GitHub ','5'), 
               ]

for per in perfiles:
    p = Perfil()
    p.descripcio = per[0]
    p.puntuacio = per[1]
    p.save()
    
    
    
    
    
    
    
    
    
    
    
    
    
    


