from pdfminer.high_level import extract_text
import os

text = extract_text("pdfs/0849882.pdf")

nombre_txt = "0849882" + ".txt"

# Crea un archivo pa meter el text si no existe
if not os.path.exists(nombre_txt):
    os.mknod(nombre_txt)

open(nombre_txt, "w").close()     # borra el contenido de metadatos.json

with open(nombre_txt, 'a') as f:  # escribe el .json
        json.dump(resultados, f)
        f.write('\n')