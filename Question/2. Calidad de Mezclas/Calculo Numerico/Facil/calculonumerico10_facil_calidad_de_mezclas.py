import svgwrite
import random

def generar_pregunta_masa_total_mezcla_aceite_vinagre():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la masa de aceite y vinagre en gramos
    masa_aceite_gramos = random.uniform(50, 300)
    masa_vinagre_gramos = random.uniform(50, 300)

    # Calcula la masa total de la mezcla
    masa_total_gramos = masa_aceite_gramos + masa_vinagre_gramos

    # Enunciado de la pregunta
    enunciado = f"Si mezclas {masa_aceite_gramos:.2f} gramos de aceite con {masa_vinagre_gramos:.2f} gramos de vinagre, ¿cuál es la masa total\n de la mezcla?"
    hint = "La masa total de la mezcla se obtiene simplemente sumando las masas del aceite y el vinagre."

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
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_masa_total_mezcla_aceite_vinagre()
