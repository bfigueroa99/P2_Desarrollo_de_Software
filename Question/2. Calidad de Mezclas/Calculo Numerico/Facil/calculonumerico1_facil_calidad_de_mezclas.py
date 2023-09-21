import svgwrite
import random

def generar_pregunta_calculo_fraccion_de_mezcla():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Volumen de agua (200 ml) y volumen de jugo de naranja (300 ml)
    volumen_agua_ml = 200
    volumen_jugo_ml = 300

    # Calcula la fracción que corresponde al agua
    fraccion_agua = volumen_agua_ml / (volumen_agua_ml + volumen_jugo_ml)

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de {volumen_agua_ml} ml de agua y {volumen_jugo_ml} ml de jugo de naranja. ¿Cuál es la fracción \nde la mezcla que corresponde al agua?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {fraccion_agua:.2f}"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_fraccion_de_mezcla()
