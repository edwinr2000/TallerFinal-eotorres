from flask import Blueprint, jsonify
from api.Models.animal import Gato, Perro, Huron, BoaConstrictor

# Crear el Blueprint para las rutas relacionadas con animales
animals_bp = Blueprint('animals', __name__)

@animals_bp.route('/animal/<nombre>', methods=['GET'])
def obtener_sonido(nombre):
    """
    Endpoint que devuelve el sonido de un animal basado en su nombre.
    """
    # Diccionario de animales disponibles
    animales = {
        "gato": Gato(),
        "perro": Perro(),
        "huron": Huron(),
        "boa constrictor": BoaConstrictor()
    }

    # Buscar el animal en el diccionario
    animal = animales.get(nombre.lower())
    if not animal:
        # Devolver un error si el animal no existe
        return jsonify({"error": "Animal no encontrado"}), 404

    # Devolver el nombre del animal y su sonido
    return jsonify({"nombre": animal.nombre, "sonido": animal.hacer_sonido()})
