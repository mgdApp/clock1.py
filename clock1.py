import time
import os

def clear_console():
    # Limpia la consola según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()
    # Obtiene la hora actual en formato HH:MM:SS
    current_time = time.strftime("%H:%M:%S")
    print("La hora actual es:", current_time)
    # Espera 1 segundo antes de actualizar
    time.sleep(1)