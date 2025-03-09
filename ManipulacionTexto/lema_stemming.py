import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
import ssl 

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Lista de palabras a lematizar
texto = ["running", "ran", "runs", "runner","runned","runs"]

# Descarga los recursos necesarios de NLTK
nltk.download('wordnet')
nltk.download('omw-1.4')    

# Crea un lematizador de WordNet
lematizador = WordNetLemmatizer()

# Lematiza cada palabra en la lista 'texto' como verbo
lemas = [lematizador.lemmatize(palabra, wordnet.VERB) for palabra in texto]

# Imprime la lista de lemas
print(lemas)

"""
El stemming es el proceso de reducir las palabras a su raíz o forma base. 
A diferencia de la lematización, que utiliza un diccionario para encontrar 
la forma base correcta de una palabra, el stemming simplemente corta los sufijos 
y prefijos para obtener la raíz. Esto puede resultar en palabras que no son 
necesariamente correctas desde el punto de vista lingüístico, pero que son 
útiles para ciertas aplicaciones como la búsqueda de texto.

"""
# Lista de palabras en español a las que se les aplicará el stemming
texto1 = ["corriendo", "corrió", "corre", "corredor", "corriendo", "corre"]

# Crea un objeto SnowballStemmer para el idioma español
stemmer = SnowballStemmer("spanish")

# Aplica el stemming a cada palabra en la lista 'texto1' y guarda las raíces en la lista 'raices'
raices = [stemmer.stem(palabra) for palabra in texto1]

# Imprime la lista de raíces obtenidas después de aplicar el stemming
print(raices)




