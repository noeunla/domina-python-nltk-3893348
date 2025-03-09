import nltk
from nltk.tokenize import word_tokenize
import ssl

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Texto a procesar
texto = "Carlos esta aprendiendo sobre procesamiento de lenguaje natural"

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Tokeniza el texto en palabras
palabras_tokenizadas = word_tokenize(texto)

# Realiza el etiquetado gramatical (POS tagging) de las palabras tokenizadas
pos_tags = nltk.pos_tag(palabras_tokenizadas)

# Imprime las palabras tokenizadas junto con sus etiquetas gramaticales
print(pos_tags)
