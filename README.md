# Regions and Countries Information

_Python Tech Test | Zinobe_

## Descripción 🚀

_Se realiza la solucion por medio de la libreria pandas para la gestion del dataframe, sqlite3 para la gestion de la base de datos y para la gestion de las peticiones a las API's se hizo uso de requests_

### Proyecto elaborado con Python 3


### Pre-requisitos 📋

_La solucion fue elaborada en un equipo con sistema operativo Ubuntu, espero que no cambie mucho la ejecucion de los comandos en otro sistema operativo_

__En la raiz del proyecto instale las librerias necesarias para la ejecucion de la solucion. Porsupuesto luego de crear el entorno virtual__


```
sebastian@sebastian:~$ python -m pip install -r requirements-txt
```

### Creacion de variable de entorno APIKEY

__Para la agilidad al momento de poner en marcha el proyecto, he decidido solo manejar el apikey en variable de entorno. Dejando por fuera las urls.__

_El api key es para el API rapidapi (https://rapidapi.com/apilayernet/api/rest-countries-v1)_

_Debe estar activo el entorno virtual de desarrollo_

```
sebastian@sebastian:~$ export APIKEY='{AQUI VA EL KEY DE ACCESO AL API}'
```


### Puesta en marcha de la solución 🔧

_Una vez tienes activado el entorno virtual de desarrollo e instaladas las dependencias (Paso anterior) Pondremos en marcha la solucion._

_En la raiz del proyecto lo podras ejecutar escribiendo el siguiente comando_

```
sebastian@sebastian:~$ python main.py
```

## Ejecutando las pruebas ⚙️

_Para ejecutar los test unitarios deberas ejecutar el fichero tests.py_

```
sebastian@sebastian:~$ python tests.py
```

### Tabla de solución 🔩

_Desglosamiento del problema en requerimientos_

|Numero de requerimiento|Descripción|Entradas|Resultados|
|---------------|-------------|--------------|----------|
|001|Gestionar la conexión con el API de rapidapi|url del API|Obtencion de una conexion estable con la 1 de las fuentes de informacion para nuestro problema (API)|
|002|Gestion y obtencion de las regiones comunes en las ciudades y de esta forma obtener un listado simplificado de regiones||Listado de las regiones|
|003|Gestion de la conexion con el API de restcountries|url del API| Conexion estable con  1 de las fuentes de información|
|004|Obtencion de 1 pais por region (Obtenida en el requerimiento 002)|Nombre de la region|Listado de paises por Region|
|005|Gestion de encriptado de un string pasado por parametro|string a encriptar|string encriptado en hexadecimal|
|006|Gestion para obtener el idioma de cada pais|pais|Idioma de cada pais|
|007|Gestion de contabilizacion del tiempo de ejecucion por linea creada en el dataframe|Fechas de la zona horaria del servidor|Timepo en segundos de la ejecucion|
|008|Gestion de la informacion obtenida y conversion a Dataframe|Informacion obtenida en los requerimientos anteriores|DataFrame con la información|
|009|Mostrar informacion relacionada con la sumatoria, minimo, maximo y tiempo promedio de ejecucion|Informacion del Dataframe|sumatoria, minimo, maximo y tiempo promedio|
|010|Gestion de conexion y operaciones con la base de datos||Base de datos creada y funciones listas para la interaccion con la base de datos|
|011|Guardar la informacion del Dataframe en una base de datos Sqlite3|Informacion de Dataframe|Persistencia de datos|
|012|Guardado de informacion del Dataframe en un archivo Json haciendo uso de funcionalidades de la libreria pandas|Informacion Dataframe|Archivo Json en directorio especial para datos|


## Construido con 🛠️


* [Python 3](https://www.python.org/) - Lenguaje de programacion
* [Pandas](https://pandas.pydata.org/) - Libreria de gestion de datos


## Autor ✒️

* **Sebastian Ayala Gonzalez** - *Backend Developer* - [website](https://websitesebas.herokuapp.com/home/)

