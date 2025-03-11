import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import ssl

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')

# Lista de documentos a procesar
documentos = [
    "la nueva aplicacion es rapida e intuitiva",
    "la aplicacion es facil de usar y muy util",
    "Me encanta la interfaz rapida de la aplicacion"
]

# Crea un vectorizador TF-IDF
vectorizador = TfidfVectorizer()

# Ajusta y transforma los documentos en una matriz TF-IDF
x = vectorizador.fit_transform(documentos)

# Imprime los nombres de las características (palabras)
print(vectorizador.get_feature_names_out())

# Imprime la matriz TF-IDF
print(x.toarray())
