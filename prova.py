from posts.models import Post
 

p = Post()
p.titol = 'Rutes de 4x4 per Palau-Savardera'
p.data = '2000-02-02'
p.descripcio = 'Una ruta molt emocionant de 30 segons','Una ruta molt emocionant de 30 segons'
p.dificultat = 'EX'

p.save()