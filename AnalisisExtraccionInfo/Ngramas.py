import nltk
from nltk.tokenize import word_tokenize
from nltk import ngrams
from collections import Counter

# Texto a procesar
texto = "la nueva aplicacion es rapida, intuitiva y facil de usar. La aplicacion es muy util y rapida"

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')

# Tokeniza el texto en palabras y convierte a minúsculas
tokens = word_tokenize(texto.lower())

# Genera bigramas (pares de palabras consecutivas)
bigramas = list(ngrams(tokens, 2))

# Genera trigramas (tripletes de palabras consecutivas)
trigramas = list(ngrams(tokens, 3))

# Calcula la frecuencia de los bigramas
frecuencia_bigramas = Counter(bigramas)

# Calcula la frecuencia de los trigramas
frecuencia_trigramas = Counter(trigramas)

# Imprime la frecuencia de los bigramas
print("Bigramas:", frecuencia_bigramas)

# Imprime la frecuencia de los trigramas
print("Trigramas:", frecuencia_trigramas)

# FRECUENCIA DE PALABRAS
# Calcula la frecuencia de las palabras

texto1 = "la IA esta revolucionando el mundo, la IA es el futuro"
tokens1 = word_tokenize(texto1)
frecuencia_palabras = Counter(tokens1)

print("Frecuencia de palabras:", frecuencia_palabras) 
