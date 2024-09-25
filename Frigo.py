class Carne:
    def __init__(self, tipo, corte, kilos):
        self.tipo = tipo
        self.corte = corte
        self.kilos = kilos

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carne_solicitada = []

    def solicitar_carne(self, carne):
        self.carne_solicitada.append(carne)

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

class Provincia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudades = []

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad)

def crear_remito(provincia):
    remito = {
        "provincia": provincia.nombre,
        "total_kilos": 0,
        "kilos_bovina": 0,
        "kilos_porcina": 0,
        "ciudades": []
    }
    for ciudad in provincia.ciudades:
        ciudad_data = {
            "nombre": ciudad.nombre,
            "total_kilos": 0,
            "kilos_bovina": 0,
            "kilos_porcina": 0,
            "clientes": []
        }
        for cliente in ciudad.clientes:
            cliente_data = {
                "nombre": cliente.nombre,
                "total_kilos": sum(carne.kilos for carne in cliente.carne_solicitada),
                "kilos_bovina": sum(carne.kilos for carne in cliente.carne_solicitada if carne.tipo == "bovina"),
                "kilos_porcina": sum(carne.kilos for carne in cliente.carne_solicitada if carne.tipo == "porcina"),
                "detalles": [(carne.tipo, carne.corte, carne.kilos) for carne in cliente.carne_solicitada]
            }
            ciudad_data['clientes'].append(cliente_data)
            ciudad_data['total_kilos'] += cliente_data['total_kilos']
            ciudad_data['kilos_bovina'] += cliente_data['kilos_bovina']
            ciudad_data['kilos_porcina'] += cliente_data['kilos_porcina']
        remito['ciudades'].append(ciudad_data)
        remito['total_kilos'] += ciudad_data['total_kilos']
        remito['kilos_bovina'] += ciudad_data['kilos_bovina']
        remito['kilos_porcina'] += ciudad_data['kilos_porcina']
    return remito

cortes_carne = {
    "bovina": [
        "Media Res", "Corte Magron", "Corte Cortito", "Corte Pistola Corto", "Corte Asado", "Corte Parrillero",
        "Corte Fantasma", "Corte Costeleta", "Corte Delantero c/Asado", "Corte Bolita", "Achuras - Juego Completo", "Achuras - Mollejas"
    ],
    "porcina": [
        "Media Res", "Corte Bondeola", "Corte Jamon", "Corte Paleta"
    ]
}