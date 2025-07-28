# controllers/transferencias.py

from datetime import datetime
from utils.corefiles import leer_json, escribir_json

RUTA_JUGADORES = 'data/jugadores.json'
RUTA_TRANSFERENCIAS = 'data/transferencias.json'
RUTA_EQUIPOS = 'data/equipos.json'

def transferir_jugador():
    print('\n🔄 Transferencia de Jugador')

    id_jugador = input('ID del jugador a transferir: ').strip()
    nuevo_equipo_id = input('ID del equipo destino: ').strip()
    tipo = input('Tipo de transferencia (venta/préstamo): ').strip().lower()

    jugadores = leer_json(RUTA_JUGADORES)
    equipos = leer_json(RUTA_EQUIPOS)
    transferencias = leer_json(RUTA_TRANSFERENCIAS)

    jugador = next((j for j in jugadores if j['id'] == id_jugador), None)
    if not jugador:
        print('❌ Jugador no encontrado.')
        return

    if not any(e['id'] == nuevo_equipo_id for e in equipos):
        print('❌ Equipo destino no encontrado.')
        return

    transferencia = {
        'jugador_id': id_jugador,
        'nombre_jugador': jugador['nombre'],
        'origen': jugador['id_equipo'],
        'destino': nuevo_equipo_id,
        'tipo': tipo,
        'fecha': datetime.now().strftime('%Y-%m-%d')
    }

    transferencias.append(transferencia)
    escribir_json(RUTA_TRANSFERENCIAS, transferencias)

    if tipo == 'venta':
        jugador['id_equipo'] = nuevo_equipo_id
        for i, j in enumerate(jugadores):
            if j['id'] == id_jugador:
                jugadores[i] = jugador
        escribir_json(RUTA_JUGADORES, jugadores)

    print(f'✅ Transferencia registrada: {jugador["nombre"]} -> nuevo equipo ID {nuevo_equipo_id}')

    escribir_json(RUTA_TRANSFERENCIAS, transferencias)

    if tipo == "venta":
        jugador["id_equipo"] = nuevo_equipo_id
        for i, j in enumerate(jugadores):
            if j["id"] == id_jugador:
                jugadores[i] = jugador
        escribir_json(RUTA_JUGADORES, jugadores)

    print(f"✅ Transferencia registrada: {jugador['nombre']} -> nuevo equipo ID {nuevo_equipo_id}")
