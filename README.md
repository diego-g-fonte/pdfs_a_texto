Esto tiene el propósito de, primero, averiguar cómo transformar un pdf a texto
procesable (tal vez haya varias formas, cada una con sus ventajas), y, segundo,
automatizar ese proceso para de hecho tener una base de datos usable.

pdfs/0.py es el que produce plaintext.json. Se tiene que correr desde 
pdfs_a_texto. Me salió de chiripa pero ya está.
    Input: pdfs/ (un folder con todos los pdfs)
    Output: plaintext.json (un json con {"doc_num": "x", "texto": "y"})

plaintext.json tiene todos los trabajos de titulación junto con sus doc_nums.

Creo que vale la pena limpiarlo (porque todo está en una sola línea). Luego hay
que unirlo con el resto de metadatos (que en realidad creo que conviene que
sean solo el doc_num, el título y el año. Es decir, sin el nombre)

### COSAS QUE PENSÉ SOBRE LA CUANTIFICACIÓN DE ESTOS TEXTOS ###

Hay que considerar:
    - En 0650836.pdf, por ejemplo, hay fotocopias del texto original (es
    una traducción comentada) que generan un montón de líneas de texto
    incoherente. 
        SOLUCIÓN: 
            1. ignorarlo
            2. manualmente quitar esas secciones
            3. hacer un script que reconozca los "OCR interpretations" y los
            elimine.
    - Los números de página
    - Las notas al pie de página (chance esto se puede solucionar tomando
    en cuneta que estas secciones no están separadas por dos líneas como
    el texto normal. Esto por sí solo no notaría las notas al pie que
    sólo son de una línea y que no están acompañadas por otra nota. Además,
    no funciona para todos los textos, por ejemplo "0849882.pdf". Creo que
    más bien va a tener que ser algo con la proximidad de los números a las
    letras. No sé, voy a tener que hacer un montón de prueba y error. Ahora
    que lo pienso esto va después de pasarlo todo a texto plano.)
    - Tengo trabajos del SUA también, no sé si considerarlos o excluirlos.

### SOLUCIONADO ###
ARREGLAR: hay unos pdfs (me imagino que los más viejos) que hacen que pdfminer
saque el error "Data-loss while decompressing corrupted data". No sé qué pex
    El límite es 0629932.pdf. Del inicio hasta 0628716.pdf todos dicen el mismo
    error. Los que tienen la terminación "_A1" también sacan el error. Estos
    48 trabajos. También hay algunos otros que sacan el mismo error.
        POSIBLE SOULCIÓN: Chance se soluciona si descargo otra vez los pdfs?
        Hay que descargar un par manualmente y testear

SOLUCIÓN: En vez de pdfminer.six, hay que usar PyMuPDF.

Guardar esto en github. (entender bien y con tiempo cómo funciona eso de las
keys)

0.py es uno para testear
Creo que conviene lo que hace PyMuPDF de guardar la información de cada página
como un elemento independiente, entonces hay que
    1. matchear cada texto con su respectivo título y año. Esto se hace con el
    doc_num.
        1.1 Sacar el doc_num como parte de la lista
    2. iterar sobre cada archivo
    3. desarrollar una manera de hacer una lista nesteada en el json
        3.1 leer el json a una lista en python y luego 
        3.2 namás appendearle la lista nesteada.

[ESTO RESULTÓ SER IRRELEVANTE] 1.py pretende iterar cada .pdf y sacar un .txt.
hay que solucionar 0.py antes
