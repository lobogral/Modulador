from sys import argv
from importador import importarRepositorio
from ejecutor import ejecutarModulo
from agregador import agregarRepositorio

import os

opcion = argv[1]

if opcion == '-i':
    urlRep = argv[2]
    importarRepositorio(urlRep)    
elif opcion == '-e':
    nombreModRep = argv[2]
    argv = argv[2:]
    ejecutarModulo(nombreModRep, argv)
elif opcion == '-a':
    tieneModulos = argv[2]
    urlRep = argv[3]
    agregarRepositorio(tieneModulos, urlRep)
else:
    print("Opción", opcion, "no disponible")
