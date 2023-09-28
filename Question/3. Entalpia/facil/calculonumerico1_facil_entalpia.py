import svgwrite
import random

def generar_pregunta_cambio_entalpia_reaccion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor conocido del cambio de entalpía de la reacción en kJ
    cambio_entalpia =random.uniform(-500, 500)

    # Enunciado de la pregunta
    enunciado = f"Si una reacción química libera {abs(cambio_entalpia)} kJ de calor, ¿cuál es el cambio de entalpía (ΔH) de la reacción?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cambio_entalpia} kJ"

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return cambio_entalpia, respuesta

# Llama a la función y guarda la respuesta
cambio_entalpia, respuesta = generar_pregunta_cambio_entalpia_reaccion()

