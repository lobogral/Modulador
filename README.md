# pymportparal
Importa repositorios de git como módulos python en modo desarrollo de forma paralela.

Por ejemplo, si el árbol de dependencias de un programa en python es de esta manera:

```
programa
│    dependencia_1
│    dependencia_git_1   
│
└───dependencia_git_2
        dependencia_git_1
        dependencia_2
```

Al utilizar pymportparal las dependencias simples (No tienen repositorio git) se importan normalmente, y las dependencias que son
repositorios de git, se instalan en la carpeta donde se usó el comando en modo desarrollo sin repetir importaciones.

## Instalación

Para instalar la versión más reciente de ``pymportparal`` usando pip:

1. Descargar el archivo .tar.gz mediante el siguiente [link](https://github.com/lobogral/pymportparal/releases/latest/download/pymportparal.tar.gz).

2. Ejecutar el comando:

        $ pip install pymportparal.tar.gz

Si se desea instalar para desarrollo, ejecutar lo siguiente:

    $ git clone https://github.com/lobogral/pymportparal.git
    $ cd pymportparal
    $ pip install -e .
    
## Ejecución

Sólo es necesario escribir el comando junto al repositorio al que se le desean descargar las dependencias, por ejemplo:

    $ pymportparal https://github.com/lobogral/ejercicios_estadistica
