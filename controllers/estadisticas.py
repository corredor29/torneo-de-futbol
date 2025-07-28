# controllers/estadisticas.py

from utils.corefiles import leer_json

RUTA_EQUIPOS = 'data/equipos.json'
RUTA_JUGADORES = 'data/jugadores.json'
RUTA_TRANSFERENCIAS = 'data/transferencias.json'

def mostrar_estadisticas():
    print('\n📊 Estadísticas Generales')

    equipos = leer_json(RUTA_EQUIPOS)
    jugadores = leer_json(RUTA_JUGADORES)
    transferencias = leer_json(RUTA_TRANSFERENCIAS)

    print(f'🏟️ Total de equipos registrados: {len(equipos)}')
    print(f'👥 Total de jugadores registrados: {len(jugadores)}')
    print(f'🔁 Total de transferencias registradas: {len(transferencias)}')

    print('\n👤 Jugadores por equipo:')
    for equipo in equipos:
        jugadores_en_equipo = [j for j in jugadores if j['id_equipo'] == equipo['id']]
        print(f'- {equipo["nombre"]}: {len(jugadores_en_equipo)} jugador(es)')
