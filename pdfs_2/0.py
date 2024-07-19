# Esto es un test. Usa PyMuPDF para copiar el texto

from pdfminer.high_level import extract_text
import os
import fitz

doc_num = "0675808_A1"     # 0629932 sí 0628716 no
doc_dir = "pdfs/" + doc_num + ".pdf"

text_full_l = []

doc = fitz.open(doc_dir) # open a document
for page in doc: # iterate the document pages
    text = page.get_text() # get plain text encoded as UTF-8
    text_full_l.append(text)

text_full_s = str(text_full_l)

print(text_full_l)

#nombre_txt = doc_num + ".txt"
#
## Crea un archivo pa meter el text si no existe
#if not os.path.exists(nombre_txt):
#    os.mknod(nombre_txt)
#
#open(nombre_txt, "w").close()
#
#with open(nombre_txt, 'w') as f:  # escribe el .txt
#        f.write(text)