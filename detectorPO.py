from urllib import request
from urllib.error import URLError

lpo = ["coño", "hola", "damian", "pinche", "estupido", "estupida"]

def verificar_web(url):
    try:
        # Petición con User-Agent para evitar el bloqueo del sitio web
        req = request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        f = request.urlopen(req)
    except URLError:
        return ('¡La url ' + url + ' no existe!')
    else:
        aux = f.read()
        contenido = aux.split()
        palabras_encontradas = []
        
        for l in lpo:
            for con in contenido:
                if l in con.decode('utf-8', errors='ignore'):
                    # Valida que la palabra no se haya añadido previamente
                    if l not in palabras_encontradas:
                        palabras_encontradas.append(l)
                    
        return palabras_encontradas

url = 'https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print("\n-----------------------------------\n")
print("\nInforme de sitio:")
print(verificar_web(url))