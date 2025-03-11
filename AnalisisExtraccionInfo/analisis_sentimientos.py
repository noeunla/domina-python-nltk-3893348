import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import ssl

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Descarga los recursos necesarios de NLTK
nltk.download('vader_lexicon')

# Texto a analizar
text = "I love the product, but it's too expensive."

# Crea una instancia del analizador de sentimientos VADER
sentiment_analyzer = SentimentIntensityAnalyzer()

# Calcula las puntuaciones de polaridad del texto
puntuacion = sentiment_analyzer.polarity_scores(text)

# Imprime las puntuaciones de polaridad
print(puntuacion)
