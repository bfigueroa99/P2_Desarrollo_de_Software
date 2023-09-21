import svgwrite
import random

def generar_pregunta_proporcion_mezcla_harina_azucar():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera un valor aleatorio para la cantidad total de la mezcla en gramos
    cantidad_total_gramos = random.uniform(100, 500)

    # Calcula la cantidad de harina y azúcar en la mezcla en una proporción de 3:2
    cantidad_harina_gramos = (3 / 5) * cantidad_total_gramos
    cantidad_azucar_gramos = (2 / 5) * cantidad_total_gramos

    # Enunciado de la pregunta
    enunciado = f"Tienes {cantidad_total_gramos:.2f} gramos de una mezcla de harina y azúcar en una proporción de 3:2. \n¿Cuántos gramos de harina y cuántos gramos de azúcar tienes en la mezcla?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Tienes {cantidad_harina_gramos:.2f} gramos de harina y {cantidad_azucar_gramos:.2f} gramos de azúcar en la mezcla."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_proporcion_mezcla_harina_azucar()
