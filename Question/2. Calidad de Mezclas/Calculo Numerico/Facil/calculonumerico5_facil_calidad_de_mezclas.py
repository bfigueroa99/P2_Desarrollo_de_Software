import svgwrite
import random

def generar_pregunta_cantidad_de_leche_en_mezcla():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la cantidad total de la mezcla en mililitros (entre 100 ml y 1000 ml)
    cantidad_mezcla_ml = random.uniform(100, 1000)

    # Calcula la cantidad de leche en la mezcla, considerando que es 3 partes de leche y 1 parte de café
    cantidad_leche_ml = (3 / 4) * cantidad_mezcla_ml

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de 3 partes de leche y 1 parte de café. Si tienes {cantidad_mezcla_ml:.2f} ml de esta m-\nezcla, ¿cuántos ml de leche hay en total?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cantidad_leche_ml:.2f} ml"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_cantidad_de_leche_en_mezcla()
