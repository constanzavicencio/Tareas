# Tarea 1: DCCiudad 🚈🐈

## Consideraciones generales :octocat:

Por tiempo, solo se realizó parcialmente las funciones de la clase ```RedMetro``` en el módulo ```red.py```.

### Cosas implementadas y no implementadas :white_check_mark: :x:
#### 🟠 Funcionalidades
Se completaron algunas funciones, pero otras no:

* ✅ informacion_red

* ✅ agregar_tunel

* ✅ tapar_tunel

* ✅ invertir_tunel

* ✅ nivel_conexiones
            
* 🟠 rutas_posibles: Un test falla

* ❌ ciclo_mas_corto

* ❌ estaciones_intermedias

* ❌ estaciones_intermedias_avanzado

* ❌ cambiar_planos

* ❌ asegurar_ruta

#### ❌ Menú de Acciones
#### ✅ Modularización
#### ✅ PEP8


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```todos_tests.py```, dado que no tuve tiempo de hacer el menú

Para que el módulo funcione:

1. Deben existir todos los tests de la carpeta ```test_publicos```

2. Deben existir los archivos de la carpeta ````data```

3. Debe existir el archivo ```dcciudad.pyc```


Además, la versión de Python utilizada debe ser ```3.11.x``` con x mayor o igual a 7


## Librerías :books:
### Librerías externas utilizadas
La única librería nueva que se implementa es ```collections.deque``` la cual se implementa en el módulo ```red.py```, sin embargo no es necesario instalarla (viene instalada con Python)

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```red```: Contiene a ```RedMetro```