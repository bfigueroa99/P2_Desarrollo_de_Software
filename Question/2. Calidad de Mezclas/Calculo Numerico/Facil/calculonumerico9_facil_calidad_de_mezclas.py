import svgwrite
import random

def generar_pregunta_cantidad_de_jugo_de_uva_en_mezcla():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen total de la mezcla en mililitros (entre 100 ml y 1000 ml)
    volumen_mezcla_ml = random.uniform(100, 1000)

    # Calcula la cantidad de jugo de uva en la mezcla, considerando que es 40% de la mezcla
    cantidad_jugo_uva_ml = 0.4 * volumen_mezcla_ml

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de 60% de jugo de manzana y 40% de jugo de uva. Si tienes {volumen_mezcla_ml:.2f}\n ml de esta mezcla, ¿cuántos ml de jugo de uva contiene?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cantidad_jugo_uva_ml:.2f} ml"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_cantidad_de_jugo_de_uva_en_mezcla()
