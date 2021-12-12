"""Agrega aspectos a repositorio.

Importa un repositorio, agrega los archivos mínimos de un
paquete de python al repositorio, y consolida el repositorio
"""
import os


def agregar_repositorio(url_rep: str) -> None:
    """Realiza lo que esta descrito en el módulo.

    Parameters
    ----------
    url_rep
        URLs del repositorio
    """

    os.system('git clone ' + url_rep)
    nombre_rep = url_rep.split('/').pop()

    os.chdir(nombre_rep)
    os.mkdir(nombre_rep)
    os.chdir(nombre_rep)

    with open("hola_mundo.py", 'w', encoding='utf8') as arch:
        arch.write("print('Hola mundo')")

    os.chdir('..')

    with open(".gitignore", 'w', encoding='utf8') as arch:
        arch.write("__pycache__")
        arch.write("\ndist")
        arch.write("\n" + nombre_rep + ".egg-info")

    with open("setup.py", 'w', encoding='utf8') as arch:
        arch.write("from setuptools import setup, find_namespace_packages")
        arch.write("\n")
        arch.write("\nsetup(")
        arch.write("\n    name='" + nombre_rep + "',")
        arch.write("\n    version='0.1',")
        arch.write("\n    packages=find_namespace_packages(),")
        arch.write("\n)")

    os.system('git add .')
    os.system('git commit -m "Agrego esqueleto"')
