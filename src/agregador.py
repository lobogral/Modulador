import os

def agregarRepositorio(tieneModulos, repositorio):
    
    os.chdir('../codes')

    os.system('git clone ' + repositorio)

    os.chdir(repositorio.split('/').pop())
    os.mkdir('src')
    os.chdir('src')

    arch = open("holaMundo.py", "w")
    arch.write("print('Hola mundo')")
    arch.close()

    os.chdir('..')

    arch = open(".gitignore", "w")
    arch.write("__pycache__")
    if tieneModulos=='-s': arch.write("\nmodules/")
    arch.close()

    if tieneModulos=='-s': open("deps.txt", "w").close()

    os.system('git add .')
    os.system('git commit -m "Agrego esqueleto"')