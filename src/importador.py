"""
Realiza importaciones de modulos para desarrollo
"""
from sys import path
import os
import re

def __importar_deps_git(urls_deps_importadas, rut_arch):
    arch = open(rut_arch, 'r')
    repositorios = re.findall('https://github.com/\w+/\w+', arch.read())
    urls_deps_importar = [linea_arch.rstrip('\n') for linea_arch in repositorios]
    urls_deps_importar = [val for val in urls_deps_importar if val not in urls_deps_importadas]
    arch.close()
    
    for url_dep_importar in urls_deps_importar:
        if url_dep_importar not in urls_deps_importadas:
            nombre_rep_dep = url_dep_importar.split('/').pop()
            rut_arch = nombre_rep_dep + '\setup.py'
            os.system('git clone ' + url_dep_importar)
            os.system('pip install --no-deps -e ' + nombre_rep_dep)
            urls_deps_importadas += [url_dep_importar]
            if os.path.isfile(rut_arch):
                urls_deps_importadas = __importar_deps_git(urls_deps_importadas, rut_arch)

    return urls_deps_importadas

def importar_repositorio(url_rep):

    nombre_rep = url_rep.split('/').pop()

    # Importa el repositorio correspondiente
    os.chdir('../..')

    if (not os.path.isdir(nombre_rep)):

        os.system('git clone ' + url_rep)

        # Importa las dependencias de git
        rut_arch = ""    
        if os.path.isfile(nombre_rep + '/setup.py'):
            rut_arch = nombre_rep + "/setup.py"
        if os.path.isfile(nombre_rep + '/requirements.txt'):
            rut_arch = nombre_rep + "/requirements.txt"
    
        __importar_deps_git([], rut_arch)
