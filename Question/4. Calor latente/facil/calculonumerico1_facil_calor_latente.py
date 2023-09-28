import svgwrite
import random

def generar_pregunta_calor_latente_facil():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para el calor latente de fusión del hielo en J/g
    calor_latente_fusion = random.uniform(300, 400)  # Valor aleatorio en J/g

    # Masa de hielo a derretir en gramos
    masa_hielo_gramos = random.uniform(50, 100)  # Valor aleatorio en gramos

    # Calcula el calor requerido para derretir la cantidad especificada de hielo
    calor_requerido = calor_latente_fusion * masa_hielo_gramos

    # Enunciado de la pregunta
    enunciado = f"Si el calor latente de fusión del hielo es de {calor_latente_fusion:.2f} J/g y se derriten {masa_hielo_gramos:.2f} gramos de hielo, ¿cuánto calor se requiere?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {calor_requerido:.2f} J"

    # Agrega una pista breve
    hint = "Usa el calor latente de fusión para calcular el calor requerido."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_calor_latente_facil()

