import nltk
from nltk import word_tokenize
from nltk.probability import ConditionalFreqDist
import random
import ssl

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')

# Lee el contenido del archivo 'relato.txt'
with open('relato.txt', 'r') as file:
    text = file.read()

# Tokeniza el texto en palabras
tokens = word_tokenize(text)

# Genera bigramas (pares de palabras consecutivas) a partir de los tokens
bigrams = nltk.bigrams(tokens)

# Calcula la distribución de frecuencia condicional de los bigramas
frec_cond = ConditionalFreqDist(bigrams)

def generar_texto(texto_semilla, nro_palabras=10):
    """
    Genera texto basado en un texto semilla utilizando bigramas.
    
    Args:
        texto_semilla (str): El texto inicial para comenzar la generación.
        nro_palabras (int): El número de palabras a generar.
    
    Returns:
        str: El texto generado.
    """
    palabras = texto_semilla.split()  # Divide el texto semilla en palabras
    for _ in range(nro_palabras):
        # Obtiene las posibles palabras siguientes y sus probabilidades
        posibles_siguientes = list(frec_cond[palabras[-1]].keys())
        probabilidades = list(frec_cond[palabras[-1]].values())
        
        if posibles_siguientes:
            # Selecciona la siguiente palabra basada en las probabilidades
            siguiente_palabra = random.choices(posibles_siguientes, probabilidades)[0]
            palabras.append(siguiente_palabra)
        else:
            break  # Si no hay palabras siguientes, termina la generación de texto
    
    return ' '.join(palabras)  # Une las palabras en una cadena de texto

# Genera texto basado en el texto semilla 'el sol' y 20 palabras adicionales
texto_generado = generar_texto('el sol', nro_palabras=20)
print(texto_generado)
