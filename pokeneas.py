import random

pokeneas = [
    {
        "id": 1,
        "nombre": "Pokenea1",
        "altura": 1.2,
        "habilidad": "Volar",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea1.png",
        "frase_filosofica": "La vida es un viaje, no un destino."
    },
    {
        "id": 2,
        "nombre": "Pokenea2",
        "altura": 1.0,
        "habilidad": "Nadar",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea2.png",
        "frase_filosofica": "El conocimiento es poder."
    },
    {
        "id": 3,
        "nombre": "Pokenea3",
        "altura": 1.5,
        "habilidad": "Correr",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea3.png",
        "frase_filosofica": "La paciencia es una virtud."
    },
    # Agregar 7 Pokeneas más
    {
        "id": 4,
        "nombre": "Pokenea4",
        "altura": 1.1,
        "habilidad": "Saltar",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea4.png",
        "frase_filosofica": "La creatividad es la inteligencia divirtiéndose."
    },
    {
        "id": 5,
        "nombre": "Pokenea5",
        "altura": 1.3,
        "habilidad": "Escalar",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea5.png",
        "frase_filosofica": "La persistencia es el camino al éxito."
    },
    {
        "id": 6,
        "nombre": "Pokenea6",
        "altura": 1.0,
        "habilidad": "Camuflarse",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea6.png",
        "frase_filosofica": "La simplicidad es la máxima sofisticación."
    },
    {
        "id": 7,
        "nombre": "Pokenea7",
        "altura": 1.4,
        "habilidad": "Resistir",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea7.png",
        "frase_filosofica": "El cambio es la única constante."
    },
    {
        "id": 8,
        "nombre": "Pokenea8",
        "altura": 1.2,
        "habilidad": "Invisibilidad",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea8.png",
        "frase_filosofica": "El coraje es la resistencia al miedo."
    },
    {
        "id": 9,
        "nombre": "Pokenea9",
        "altura": 1.5,
        "habilidad": "Regenerar",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea9.png",
        "frase_filosofica": "La esperanza es la cosa con plumas."
    },
    {
        "id": 10,
        "nombre": "Pokenea10",
        "altura": 1.1,
        "habilidad": "Transformar",
        "imagen": "https://storage.googleapis.com/BUCKET_NAME/pokenea10.png",
        "frase_filosofica": "La imaginación es más importante que el conocimiento."
    }
]

def get_random_pokenea():
    return random.choice(pokeneas)
