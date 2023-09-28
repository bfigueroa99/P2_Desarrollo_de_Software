import svgwrite
import random

def generar_pregunta_cantidad_de_azucar_en_mezcla():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la cantidad total de la mezcla en gramos (entre 100 g y 500 g)
    cantidad_mezcla_gramos = random.uniform(100, 500)

    # Calcula la cantidad de azúcar en la mezcla, considerando que es 4 partes de azúcar y 1 parte de sal
    cantidad_azucar_gramos = (4 / 5) * cantidad_mezcla_gramos

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de 4 partes de azúcar y 1 parte de sal. Si tienes {cantidad_mezcla_gramos:.2f} gramos de \nesta mezcla, ¿cuántos gramos de azúcar hay en total?"
    hint = "Puedes calcular la cantidad de azúcar en la mezcla multiplicando la fracción correspondiente (4/5) por el peso total de la mezcla en gramos."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cantidad_azucar_gramos:.2f} gramos"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_cantidad_de_azucar_en_mezcla()
