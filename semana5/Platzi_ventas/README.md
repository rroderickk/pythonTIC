#### Click es un framework que nos permite aplicaciones de Command line
> utiliza decoradores @
> interfaz personalizable

### Decoradores mas importantes de click
> @click.group
> @click.command
> @click.argument
> @click.option

[referencia](https://www.youtube.com/watch?v=riQd3HNbaDk)

# PV program CRUD
```s
#* =()=> python -m venv [name_env]          #? Crear entorno virtual
#* =()=> Scripts\activate.bat               #? Activar entorno virtual
pip install --editable .                    #? Instalar todo lo de setup.py en el directorio actual de trabajo (.)
#* =()=> bash enter                         #? Activar bash(cmder)
which pv                                    #? Buscar en la ruta de ejecucion del sistema la aplicacion pv(comprobar que todo esta correcto)
pv clients create
pv clients list
pv clients update [id]
pv clients delete [id]
```



#### Manejo de errores

- try: significa que se ejecuta este código. Si es posible, solo ponemos una sola línea de código ahí como buena práctica
- except: es nuestro manejo del error, es lo que haremos si ocurre el error. Debemos ser específicos con el tipo de error que vamos a atrapar.
- else: Es código que se ejecuta cuando no ocurre ningún error.
- finally: Nos permite obtener un bloque de código que se va a ejecutar sin importar lo que pase.




#### Context manager
Los context managers son objetos de Python que proveen información contextual adicional al bloque de código. Esta información consiste en correr una función (o cualquier callable) cuando se inicia el contexto con el keyword with; al igual que correr otra función cuando el código dentro del bloque with concluye. Por ejemplo:
```py
with open(‘some_file.txt’) as f:
    lines = f.readlines()
```

Si estás familiarizado con este patrón, sabes que llamar la función open de esta manera, garantiza que el archivo se cierre con posterioridad. Esto disminuye la cantidad de información que el programador debe manejar directamente y facilita la lectura del código.

Existen dos formas de implementar un context manager: con una clase o con un generador. Vamos a implementar la funcionalidad anterior para ilustrar el punto:

```py
class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()

with CustomOpen('file') as f:
    contents = f.read()
```
Esta es simplemente una clase de Python con dos métodos adicionales: enter y exit. Estos métodos son utilizados por el keyword with para determinar las acciones de inicialización, entrada y salida del contexto.

El mismo código puede implementarse utilizando el módulo contextlib que forma parte de la librería estándar de Python.

```py
from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('file') as f:
    contents = f.read()
```
El código anterior funciona exactamente igual que cuando lo escribimos con una clase. La diferencia es que el código se ejecuta al inicializarse el contexto y retorna el control cuando el keyword yield regresa un valor. Una vez que termina el bloque with, el context manager toma de nueva cuenta el control y ejecuta el código de limpieza.



# Python tiene muchas aplicaciones:

En las ciencias tiene muchas librerías que puedes utilizar como analisis de las estrellas y astrofisica; si te interesa la medicina puedes utilizar Tomopy para analizar tomografías. También están las librerías más fuertes para la ciencia de datos numpy, Pandas y Matplotlib

En CLI por si te gusta trabajar en la nube y con datacenters, para sincronizar miles de computadoras:

> aws
> gcloud
> rebound
> geeknote
> Aplicaciones Web:

> Django
> Flask
> Bottle
> Chalice
> Webapp2
> Gunicorn
> Tornado







# import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


# importar esto

El Zen de Python, de Tim Peters

Hermoso es mejor que feo.
Explícito es mejor que implícito.
Lo simple es mejor que lo complejo.
Complejo es mejor que complicado.
Plano es mejor que anidado.
Disperso es mejor que denso.
La legibilidad cuenta.
Los casos especiales no son lo suficientemente especiales como para romper las reglas.
Aunque la practicidad le gana a la pureza.
Los errores nunca deben pasar en silencio.
A menos que se silencie explícitamente.
Frente a la ambigüedad, rechace la tentación de adivinar.
Debe haber una, y preferiblemente solo una, forma obvia de hacerlo.
Aunque esa manera puede no ser obvia al principio a menos que seas holandés.
Ahora es mejor que nunca.
Aunque nunca suele ser mejor que *ahora mismo* ahora.
Si la implementación es difícil de explicar, es una mala idea.
Si la implementación es fácil de explicar, puede ser una buena idea.
Los espacios de nombres son una gran idea, ¡hagamos más de esos!


# PEPS
> PEP8 : guia de estilo de codigo
> PEP257 : python docstrings
> PEP20 : import this



# Servidor en python

activar entorno virtual e instalar
pip install flask
pip freeze
touch requirements.txt -> versiones de las librerias version de -> flask=v
podemos instalar lo que este en requirements con :
pip install -r  requirements.txt

```py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '</h1 style="color: crimson; font-size: 20px">Hello, World!</h1>'

if __name__ == '__main__':
    app.run()
```