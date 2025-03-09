import nltk
from nltk.tokenize import word_tokenize
from nltk import ne_chunk
import ssl

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Texto a procesar
texto = "John trabaja en Linkedin desde el 2020"

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Tokeniza el texto en palabras
palabras_tokenizadas = word_tokenize(texto)

# Realiza el etiquetado gramatical (POS tagging) de las palabras tokenizadas
post_tags = nltk.pos_tag(palabras_tokenizadas)

# Realiza el reconocimiento de entidades nombradas (NER) en las palabras etiquetadas
entidades = ne_chunk(post_tags)

# Imprime las entidades reconocidas
print(entidades)
