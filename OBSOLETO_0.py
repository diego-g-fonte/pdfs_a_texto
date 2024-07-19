# Esto es como un test

from pdfminer.high_level import extract_text
import os
import threading
lock=threading.Lock()

doc_num = "0681675"     # 0629932 sí 0628716 no
doc_dir = "pdfs/" + doc_num + ".pdf"

lock.acquire()  # Esto hace algo con el threading para que no salga el error "Data-loss while decompressing corrupted data"
text = extract_text(doc_dir)
lock.release()

nombre_txt = "txts/" + doc_num + ".txt"

# Crea un archivo pa meter el text si no existe
if not os.path.exists(nombre_txt):
    os.mknod(nombre_txt)

open(nombre_txt, "w").close()

with open(nombre_txt, 'w') as f:  # escribe el .txt
        f.write(text)