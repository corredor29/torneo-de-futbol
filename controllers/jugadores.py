# controllers/jugadores.py

import uuid
from utils.corefiles import leer_json, escribir_json

RUTA_JUGADORES = 'data/jugadores.json'
RUTA_EQUIPOS = 'data/equipos.json'

def registrar_jugador():
    print('\n👤 Registro de Nuevo Jugador')
    nombre = input('Nombre del jugador: ').strip()
    posicion = input('Posición: ').strip()
    dorsal = input('Número dorsal: ').strip()
    id_equipo = input('ID del equipo: ').strip()

    # Validar que el equipo exista
    equipos = leer_json(RUTA_EQUIPOS)
    if not any(equipo['id'] == id_equipo for equipo in equipos):
        print('❌ El equipo no existe.')
        return

    jugador = {
        'id': str(uuid.uuid4()),
        'nombre': nombre,
        'posicion': posicion,
        'dorsal': dorsal,
        'id_equipo': id_equipo
    }

    jugadores = leer_json(RUTA_JUGADORES)
    jugadores.append(jugador)
    escribir_json(RUTA_JUGADORES, jugadores)

    print(f'✅ Jugador \'{nombre}\' registrado correctamente.')

def listar_jugadores():
    print('\n📄 Lista de Jugadores Registrados:')
    jugadores = leer_json(RUTA_JUGADORES)

    if not jugadores:
        print('No hay jugadores registrados.')
        return

    for idx, jugador in enumerate(jugadores, 1):
        print(f'{idx}. {jugador["nombre"]} - {jugador["posicion"]} (#{jugador["dorsal"]}) - Equipo ID: {jugador["id_equipo"]}')

    if not jugadores:
        print("No hay jugadores registrados.")
        return

    for idx, jugador in enumerate(jugadores, 1):
        print(f"{idx}. {jugador['nombre']} - {jugador['posicion']} (#{jugador['dorsal']}) - Equipo ID: {jugador['id_equipo']}")
