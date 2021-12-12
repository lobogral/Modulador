"""Hace operaciones con módulos python-git.

Hace distintas operaciones con módulos o paquetes
de python incorporados a git.
"""

from sys import argv
from pymportparal.importador import importar_repositorio

def main():

    url_rep = argv[1]
    importar_repositorio(url_rep)
