import ssl
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ssl._create_default_https_context = ssl._create_unverified_context

# Download the necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Este es un ejemplo de analisis de sentimientos donde todos los usuarios estan frustrados"

stop_words = set(stopwords.words('spanish'))
# Tokenize the text
palabras_tokenizadas = word_tokenize(text)

texto_filtrado = [palabra for palabra in palabras_tokenizadas if palabra.lower() not in stop_words]
# Print the tokens
print(texto_filtrado)