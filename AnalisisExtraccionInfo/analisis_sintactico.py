import nltk
from nltk import CFG
from nltk.parse import ChartParser
import ssl  

# Configura el contexto SSL para evitar problemas de verificación de certificados
ssl._create_default_https_context = ssl._create_unverified_context

# Descarga los recursos necesarios de NLTK
nltk.download('punkt')

# Define una gramática libre de contexto (CFG)
gramatica = CFG.fromstring("""
  S -> NP VP
  NP -> Det N | 'John' | N PP
  VP -> V NP | V PP
  PP -> P NP 
  V -> "trabaja"
  N -> "Linkedin" | "2020"
  Det -> "el"
  P -> "desde" | "en"
""")

"""
  S -> NP VP (sustantivo y verbo)
  NP -> Det N | 'John' | N PP (determinante y sustantivo, nombre propio, sustantivo y preposición)
  VP -> V NP | V PP (verbo y NP o sujeto, verbo y PP)
  PP -> P NP (preposición y sustantivo)
  V -> "trabaja"
  N -> "Linkedin" | "2020"
  Det -> "el"
  P -> "desde" | "en"
"""
# Otra gramática de ejemplo (comentada)
# gramatica = CFG.fromstring("""
#   S -> NP VP
#   NP -> Det N PP | Det N | 'Ella'
#   VP -> V NP | V PP
#   PP -> P NP
#   V -> "encontro" 
#   N -> "gato" | "mesa"
#   Det -> "un" | "la"
#   P -> "bajo"
# """)

# Crea un analizador sintáctico utilizando la gramática definida
analizador = ChartParser(gramatica)

# Oración a analizar (tokenizada)
oracion = "John trabaja en Linkedin desde el 2020".split()
# Otra oración de ejemplo (comentada)
# oracion = "Ella encontro un gato bajo la mesa".split()

# Genera los árboles sintácticos para la oración dada
arboles = list(analizador.parse(oracion))

# Si se encontraron árboles, los imprime y muestra
if arboles:
    for arbol in arboles:
        print(arbol)
        print("Arbol en formato estructurado: ")
        arbol.pretty_print()
        print("Mostrando el arbol graficamente: ")
        arbol.draw()
else:
    print("No se encontraron árboles para la oración dada")

"""
en el diagrama draw() se muestra el árbol sintáctico de la oración dada,
donde cada nodo representa un componente de la oración y las aristas
indican las relaciones entre los componentes. Los nodos internos
representan las reglas de la gramática utilizadas para analizar la oración,
mientras que las hojas representan las palabras de la oración.

S es la oracion completa, dividida en NP (sustantivo) y VP (verbo)
NP es el sujeto, que puede ser un determinante y un sustantivo, un nombre propio o un sustantivo seguido de una preposición
VP es el predicado, que puede ser un verbo seguido de un sustantivo o un verbo seguido de una preposición
PP es una preposición seguida de un sustantivo
V es el verbo "trabaja"
N son los sustantivos "Linkedin" y "2020"
Det es el determinante "el"
P son las preposiciones "desde" y "en"

"""