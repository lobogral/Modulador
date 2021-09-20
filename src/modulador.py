from sys import argv
from importador import importarRepositorio
from ejecutor import ejecutarModulo
from agregador import agregarRepositorio

import os

opcion = argv[1]

if opcion == '-i':
    urlRep = argv[2]
    importarRepositorio(urlRep)

    if not os.path.isdir('entVir'):
        os.system("py -m venv entVir")
    os.system("call entVir\Scripts/activate.bat & pip list & py Grafica.py & deactivate")
    os.system("pip list")
    
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
