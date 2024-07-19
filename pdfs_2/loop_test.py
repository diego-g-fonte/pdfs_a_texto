# Esto es para testear cómo appendear listas embebidas en json
# Funciona, pero no sé cómo hacerle para pasarlo todo al json
# Hay que darle buen formato a la lista antes de dumpearlo al json.

import json
import os
import fitz
import re

# lista = []
# a_embeber = [["a", "b"], ["c", "d"], ["e", "f", "g", "h"], ["i"], ["j", "k", "l", "m"]]
# contador = 0
# 
# for n in a_embeber:
#     lista.append([])
#     lista[contador].append(a_embeber[contador])
#     contador = contador + 1
# 
# print(lista)

# YA CON PDFS EN EL DIRECTORIO PDFS_2/PDFS

# assign directory. Necesitas esto para que os.listdir() funcione
directory = 'pdfs'  # Es sin "/"

contador = 0    # Es necesario para indicar el elemento de la lista en textos y que quede nesteado.
textos = []
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    doc = fitz.open("pdfs/" + filename) # open a document
    doc_num = re.sub(".pdf", "", filename)

    textos.append([])
    for page in doc: # iterate the document pages
        text = page.get_text() # get plain text encoded as UTF-8
        textos[contador].append({"doc_num": doc_num, "texto": text})
    contador = contador + 1

# Crea plaintext.json si no existe
if not os.path.exists('plaintext.json'):
    os.mknod('plaintext.json')

open("plaintext.json", "w").close()     # borra el contenido de plaintext.json

with open('plaintext.json', 'a') as f:  # escribe el .json
        json.dump(textos, f)
        f.write('\n')

print(len(textos))