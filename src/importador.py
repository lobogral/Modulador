"""Realiza importaciones de módulos.

Realiza importaciones de módulos o paquetes git en
forma de árbol para desarrollo en pip

Note
----
Solo realiza las importaciones de módulos git
para importar otro tipo de módulos, se debe hacer
manualmente
"""
import os
import re


def __importar_deps_git(urls_deps_importadas: list[str],
                        rut_arch: str) -> list[str]:
    """Método privado, importa las dependencias de git.

    Parameters
    ----------
    url_deps_importadas
        URLs de las dependencias importadas
    rut_arch
        Ruta del archivo

    Returns
    -------
    list[str]
        URLs de las dependencias importadas
    """
    with open(rut_arch, 'r', encoding='utf8') as arch:
        repositorios = re.findall('https://github.com/\\w+/\\w+', arch.read())
        urls_deps_importar = [linea_arch.rstrip('\n')
                              for linea_arch in repositorios]
        urls_deps_importar = [val
                              for val in urls_deps_importar
                              if val not in urls_deps_importadas]

    for url_dep_importar in urls_deps_importar:
        if url_dep_importar not in urls_deps_importadas:
            nombre_rep_dep = url_dep_importar.split('/').pop()
            rut_arch = nombre_rep_dep + '\\setup.py'
            os.system('git clone ' + url_dep_importar)
            os.system('pip install --no-deps -e ' + nombre_rep_dep)
            urls_deps_importadas += [url_dep_importar]
            if os.path.isfile(rut_arch):
                urls_deps_importadas = __importar_deps_git(
                    urls_deps_importadas,
                    rut_arch)

    return urls_deps_importadas


def importar_repositorio(url_rep: str) -> None:
    """Hace la importación del módulo git principal.

    Parameters
    ----------
    url_rep
        URL del repositorio
    """
    nombre_rep = url_rep.split('/').pop()

    # Importa el repositorio correspondiente
    os.chdir('../..')

    if not os.path.isdir(nombre_rep):

        os.system('git clone ' + url_rep)

        # Importa las dependencias de git
        rut_arch = ""
        if os.path.isfile(nombre_rep + '/setup.py'):
            rut_arch = nombre_rep + "/setup.py"
        if os.path.isfile(nombre_rep + '/requirements.txt'):
            rut_arch = nombre_rep + "/requirements.txt"

        __importar_deps_git([], rut_arch)
