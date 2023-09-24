import svgwrite
import random

def generar_pregunta_masa_total_mezcla_azucar_harina():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para las masas de azúcar y harina en gramos
    masa_azucar_gramos = random.uniform(10, 100)
    masa_harina_gramos = random.uniform(100, 500)

    # Calcula la masa total de la mezcla
    masa_total_gramos = masa_azucar_gramos + masa_harina_gramos

    # Enunciado de la pregunta
    enunciado = f"Si mezclas {masa_azucar_gramos:.2f} gramos de azúcar con {masa_harina_gramos:.2f} gramos de harina, ¿cuál es la masa total\n de la mezcla?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50 

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {masa_total_gramos:.2f} gramos"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return masa_azucar_gramos, masa_harina_gramos, respuesta

# Llama a la función y guarda la respuesta
masa_azucar_gramos, masa_harina_gramos, respuesta = generar_pregunta_masa_total_mezcla_azucar_harina()
