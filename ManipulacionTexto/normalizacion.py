import ssl
import nltk
from nltk.corpus import cess_esp
from nltk.metrics import jaccard_distance
from nltk.util import ngrams

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('cess_esp')

# Texto con errores ortográficos
texto2 = "ESTE texot tienee algunos errrores de ortografia. Devería SER corregido antes de ser puvlicado."

# Lista de palabras correctas del corpus 'cess_esp'
palabras_correctas = list(cess_esp.words())
print(len(palabras_correctas))  # Imprime la cantidad de palabras correctas disponibles

def normalizar_texto(texto):
    """
    Normaliza el texto convirtiéndolo a minúsculas, tokenizándolo y eliminando la puntuación.
    Args:
        texto (str): El texto a normalizar.
    Returns:
        str: El texto normalizado.
    """
    texto_minusculas = texto.lower()  # Convierte el texto a minúsculas
    palabras = nltk.word_tokenize(texto_minusculas)  # Tokeniza el texto en palabras
    palabras_sin_puntuacion = [palabra for palabra in palabras if palabra.isalnum()]  # Elimina la puntuación
    return ' '.join(palabras_sin_puntuacion)  # Une las palabras en una cadena de texto

def corregir_ortografia_jaccard(texto):
    """
    Corrige la ortografía de un texto utilizando la distancia de Jaccard basada en trigramas.
    Args:
        texto (str): El texto a corregir.
    Returns:
        str: El texto con las palabras corregidas.
    El algoritmo tokeniza el texto en palabras y para cada palabra que tiene al menos 3 caracteres,
    calcula la distancia de Jaccard entre los trigramas de la palabra y los trigramas de las palabras
    correctas. Si encuentra posibles correcciones, selecciona la corrección con la menor distancia de Jaccard.
    Si no encuentra posibles correcciones, deja la palabra original.
    """
    palabras = nltk.word_tokenize(texto)  # Tokeniza el texto en palabras
    palabras_corregidas = []  # Lista para almacenar las palabras corregidas

    for palabra in palabras:
        if len(palabra) < 3:  # Si la palabra tiene menos de 3 caracteres, no se corrige
            palabras_corregidas.append(palabra)
            continue

        # Calcula los trigramas de la palabra
        trigramas_palabras = set(ngrams(palabra, 3))

        # Encuentra posibles correcciones basadas en la distancia de Jaccard
        posibles_correcciones = [(jaccard_distance(trigramas_palabras, set(ngrams(w, 3))), w) 
                                for w in palabras_correctas if len(w) >= 3 and w[0] == palabra[0] and abs(len(w) - len(palabra)) <= 2]
       
        if posibles_correcciones:
            # Selecciona la corrección con la menor distancia de Jaccard
            correccion = sorted(posibles_correcciones, key=lambda x: x[0])[0][1]
            palabras_corregidas.append(correccion)
        else:
            palabras_corregidas.append(palabra)  # Si no hay correcciones, se deja la palabra original

    return ' '.join(palabras_corregidas)  # Une las palabras corregidas en una cadena de texto

# Normaliza el texto original
texto_normalizado = normalizar_texto(texto2)

# Corrige la ortografía del texto normalizado
texto_corregido = corregir_ortografia_jaccard(texto_normalizado)

# Imprime el texto original, normalizado y corregido
print(f'Texto original: {texto2}')
print(f'Texto normalizado: {texto_normalizado}')
print(f'Texto corregido: {texto_corregido}')
