import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import ssl

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Diccionario de textos en diferentes idiomas
textos = {
    "es": "Este es un ejemplo de análisis de sentimientos donde todos los usuarios están frustrados",
    "en": "This is an example of sentiment analysis where all users are frustrated", 
    "fr": "C'est un exemple d'analyse de sentiment où tous les utilisateurs sont frustrés"
}

# Procesa cada texto en el diccionario
for idioma, texto in textos.items():
    # Tokeniza el texto en palabras, especificando el idioma para el tokenizador
    tokens = word_tokenize(texto, language="spanish" if idioma == "es" else "english")

    # Selecciona las palabras vacías según el idioma
    if idioma == "es":
        stop_words = set(stopwords.words('spanish'))
    elif idioma == "en":
        stop_words = set(stopwords.words('english'))
    elif idioma == "fr":
        stop_words = set(stopwords.words('french'))
    else:
        stop_words = set()

    # Filtra las palabras vacías del texto tokenizado
    tokens_filtrados = [palabra for palabra in tokens if palabra.lower() not in stop_words]
    
    # Imprime el texto tokenizado y filtrado por idioma
    print(f"Texto en {idioma}: {tokens_filtrados}")


