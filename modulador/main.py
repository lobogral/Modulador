"""Hace operaciones con módulos python-git.

Hace distintas operaciones con módulos o paquetes
de python incorporados a git.
"""

from sys import argv
from modulador.importador import importar_repositorio
from modulador.agregador import agregar_repositorio

def main():

    opcion = argv[1]
    url_rep = argv[2]

    if opcion == '-i':
        importar_repositorio(url_rep)
    elif opcion == '-a':
        agregar_repositorio(url_rep)
    else:
        print("Opción", opcion, "no disponible")
