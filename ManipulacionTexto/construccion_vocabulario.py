import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import ssl

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Texto a procesar
texto = "El procesamiento de lenguaje natural es una rama de la inteligencia artificial que se ocupa de la interacción entre las computadoras y los humanos mediante el lenguaje natural. El objetivo del procesamiento de lenguaje natural es permitir que las computadoras comprendan, interpreten y generen lenguaje humano de manera útil."

# Tokeniza el texto en palabras y convierte a minúsculas
palabras_tokenizadas = word_tokenize(texto.lower())

# Obtiene las palabras vacías en español
stop_words = set(stopwords.words('spanish'))

# Filtra las palabras vacías del texto tokenizado
texto_filtrado = [palabra for palabra in palabras_tokenizadas if palabra.lower() not in stop_words]

# Construye un conjunto de palabras únicas (vocabulario) del texto filtrado
vocabulario = set(texto_filtrado)

# Imprime el vocabulario y el número de términos únicos
print("Vocabulario", vocabulario)
print(f'Numero de terminos unicos: {len(vocabulario)}')

