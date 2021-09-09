import os
# Principal
#rutaPrincipal = 'C:/xampp/htdocs/dashboard/Mis Proyectos/Python/Proyecto'
rutaPrincipal = 'C:/Users/xXKennerthXx/Desktop/Proyecto'
# ICO
ico = 'IMG/uptpc.ico'
uptpc = os.path.join(rutaPrincipal, ico)
uptpc = os.path.abspath(uptpc)

# Fondo
fondoDPantalla = 'IMG/fondo.png'
fondo = os.path.join(rutaPrincipal, fondoDPantalla)
fondo = os.path.abspath(fondo)

# Base de datos
routebd = 'tecnologico.db'
baseDedatos = os.path.join(rutaPrincipal,routebd)
baseDedatos = os.path.abspath(baseDedatos)
