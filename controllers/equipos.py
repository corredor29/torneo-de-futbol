# controllers/equipos.py

import os
import uuid
from utils.corefiles import leer_json, escribir_json
from utils.validateData import validar_fecha

RUTA_EQUIPOS = 'data/equipos.json'

def registrar_equipo():
    print('\n📘 Registro de Nuevo Equipo')

    nombre = input('Nombre del equipo: ').strip()
    fundacion = input('Fecha de fundación (YYYY-MM-DD): ').strip()
    pais = input('País: ').strip()
    id_liga = input('ID de la liga: ').strip()

    if not validar_fecha(fundacion):
        print('❌ Fecha inválida. Debe tener formato YYYY-MM-DD.')
        return

    equipo = {
        'id': str(uuid.uuid4()),
        'nombre': nombre,
        'fundacion': fundacion,
        'pais': pais,
        'id_liga': id_liga
    }

    equipos = leer_json(RUTA_EQUIPOS)
    equipos.append(equipo)
    escribir_json(RUTA_EQUIPOS, equipos)

    print(f'✅ Equipo \'{nombre}\' registrado correctamente.')

def listar_equipos():
    print('\n📄 Lista de Equipos Registrados:')
    equipos = leer_json(RUTA_EQUIPOS)

    if not equipos:
        print('No hay equipos registrados.')
        return

    for idx, equipo in enumerate(equipos, 1):
        print(f'{idx}. {equipo["nombre"]} ({equipo["pais"]}, Fundado: {equipo["fundacion"]}) - Liga ID: {equipo["id_liga"]}')
