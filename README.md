# clock1.py
Programa en Python que muestra la hora actual en la consola.

# Syntax

1. Importar módulos:

    - `import time`: Importa el módulo `time`, que proporciona funciones relacionadas con el tiempo. En este programa se utiliza para obtener la hora actual y pausar la ejecución durante un intervalo determinado.
    - `import os`: Importa el módulo `os`, que permite interactuar con el sistema operativo. Se utiliza para ejecutar comandos del sistema (en este caso, para limpiar la pantalla).

2. Definir una función para limpiar la consola:

```
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
```

- `os.system('cls' if os.name == 'nt' else 'clear')`: Llama al método (o a la función) `system` del módulo `os` para ejecutar un comando en el sistema operativo.

    - `'cls' if os.name == 'nt' else 'clear'`: Condicional (operador ternario) en Python.

        - Si el nombre del sistema operativo es Windows `nt`, entonces se usará el comando `cls`.
        - Sino, entonces se usará el comando clear.

3. Mostrar la hora:

```
while True:
    clear_console()
    current_time = time.strftime("%H:%M:%S")
    print("La hora acual es: ", current_time)
    time.sleep(1)
```

- `while True`: Crea un bucle infinito.
- `clear_console()`: Llama a la función que limpia la consola en cada iteración.
- `current_time = time.strftime("%H:%M:%S")`: Utiliza la función (o método) `strftime` del módulo `time` para formatear la hora actual en formato 24 horas en un string.

    - `"%H"`: Horas en formato 24 horas (00-23).
    - `"%M"`: Minutos (0-59).
    - `"%S"`: Segundos (0-59).

- `print("La hora actual es: ", current_time)`: Imprime la hora actual.
- `time.sleep(1)`: Hace que el programa se detenga (o duerma) por un segundo. En este caso, el ciclo se ejecutará cada segundo, permitiendo que el reloj se actualice cada segundo.