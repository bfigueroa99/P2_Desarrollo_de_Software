import svgwrite
import random

def generar_pregunta_fraccion_de_mezcla_agua():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para las cantidades de agua y jugo de naranja en mililitros
    cantidad_agua_ml = random.uniform(100, 500)
    cantidad_jugo_naranja_ml = random.uniform(100, 500)

    # Calcula la fracción correspondiente al agua en la mezcla
    fraccion_agua = cantidad_agua_ml / (cantidad_agua_ml + cantidad_jugo_naranja_ml)

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de {cantidad_agua_ml:.2f} ml de agua y {cantidad_jugo_naranja_ml:.2f} ml de jugo de naranja. ¿Cuál es la fr-\nacción de la mezcla que corresponde al agua?"
    hint = "La fracción de la mezcla que corresponde al agua se calcula dividiendo la cantidad de agua entre la cantidad total de líquido en la mezcla (agua + jugo de naranja)."

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
    return cantidad_agua_ml, cantidad_jugo_naranja_ml, respuesta

# Llama a la función y guarda la respuesta
cantidad_agua_ml, cantidad_jugo_naranja_ml, respuesta = generar_pregunta_fraccion_de_mezcla_agua()
