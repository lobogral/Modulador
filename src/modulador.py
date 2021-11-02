"""Hace operaciones con módulos python-git.

Hace distintas operaciones con módulos o paquetes
de python incorporados a git.
"""

from sys import argv
from importador import importar_repositorio
from agregador import agregar_repositorio

opcion = argv[1]
url_rep = argv[2]

if opcion == '-i':
    importar_repositorio(url_rep)
elif opcion == '-a':
    agregar_repositorio(url_rep)
else:
    print("Opción", opcion, "no disponible")
