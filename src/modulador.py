from sys import argv
from importador import importarRepositorio
from ejecutor import ejecutarModulo
from agregador import agregarRepositorio

opcion = argv[1]

if opcion == '-i':
    repositorio = argv[2]
    importarRepositorio(repositorio)
elif opcion == '-e':
    modulo = argv[2]
    argv = argv[2:]
    ejecutarModulo(modulo, argv)
elif opcion == '-a':
    tieneModulos = argv[2]
    repositorio = argv[3]
    agregarRepositorio(tieneModulos, repositorio)
