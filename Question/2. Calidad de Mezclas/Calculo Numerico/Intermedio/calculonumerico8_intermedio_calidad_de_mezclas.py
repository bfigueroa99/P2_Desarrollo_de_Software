import svgwrite
import random

def generar_pregunta_proporcion_nueces_almendras():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Cantidad total de la mezcla en gramos
    cantidad_total_gramos = 250

    # Proporción de nueces a almendras (variables aleatorias)
    proporcion_nueces = random.randint(2, 6)
    proporcion_almendras = random.randint(2, 6)

    # Calcula la cantidad de nueces y almendras en la mezcla
    cantidad_nueces_gramos = (cantidad_total_gramos * proporcion_nueces) / (proporcion_nueces + proporcion_almendras)
    cantidad_almendras_gramos = (cantidad_total_gramos * proporcion_almendras) / (proporcion_nueces + proporcion_almendras)

    # Enunciado de la pregunta
    enunciado = f"Tienes {cantidad_total_gramos} gramos de una mezcla de nueces y almendras en una proporción de {proporcion_nueces}:{proporcion_almendras}.\n ¿Cuántos gramos de nueces tienes en la mezcla?"
    hint = "Esta pregunta no tiene hint."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Tienes {cantidad_nueces_gramos:.2f} gramos de nueces en la mezcla."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_proporcion_nueces_almendras()
