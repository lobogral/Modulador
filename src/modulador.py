from sys import argv
from importador import importar_repositorio
from agregador import agregarRepositorio

import os

opcion = argv[1]

if opcion == '-i':
    urlRep = argv[2]
    importar_repositorio(urlRep)    
elif opcion == '-a':
    tieneModulos = argv[2]
    urlRep = argv[3]
    agregarRepositorio(tieneModulos, urlRep)
else:
    print("Opción", opcion, "no disponible")
