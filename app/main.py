
# app/main.py

import sys
sys.path.append('.') 

from controllers.equipos import registrar_equipo, listar_equipos
from controllers.jugadores import registrar_jugador, listar_jugadores
from controllers.transferencias import transferir_jugador
from controllers.estadisticas import mostrar_estadisticas

def mostrar_menu():
    print('\n=== GESTOR DE TORNEOS INTERNACIONALES ===')
    print('1. Registrar equipo')
    print('2. Listar equipos')
    print('3. Registrar jugador')
    print('4. Listar jugadores')
    print('5. Transferencia de jugador (venta o préstamo)')
    print('6. Ver estadísticas')
    print('0. Salir')

def main():
    while True:
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            registrar_equipo()
        elif opcion == '2':
            listar_equipos()
        elif opcion == '3':
            registrar_jugador()
        elif opcion == '4':
            listar_jugadores()
        elif opcion == '5':
            transferir_jugador()
        elif opcion == '6':
            mostrar_estadisticas()
        elif opcion == '0':
            print('Gracias por usar el gestor. ¡Hasta luego!')
            break
        else:
            print('Opción inválida. Intente nuevamente.')

if __name__ == '__main__':
    main()
