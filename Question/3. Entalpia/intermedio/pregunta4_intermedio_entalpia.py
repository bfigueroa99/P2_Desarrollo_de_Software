import svgwrite
import random

def generar_pregunta_cambio_entalpia_por_mol():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para el cambio de entalpía total en kJ
    cambio_entalpia_total = random.uniform(-100, 100)  # Valor aleatorio en kJ

    # Cantidad de moles de producto formado en la reacción
    moles_producto = random.uniform(0.1, 2)  # Valor aleatorio en moles

    # Calcula el cambio de entalpía por mol de producto formado
    cambio_entalpia_por_mol = cambio_entalpia_total / moles_producto

    # Enunciado de la pregunta
    enunciado = f"Si se conoce que el cambio de entalpía de una reacción es {cambio_entalpia_total:.2f} kJ y se producen {moles_producto:.2f} moles de un producto, ¿cuál es el cambio de entalpía por mol de producto formado?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cambio_entalpia_por_mol:.2f} kJ/mol"

    # Agrega una pista breve
    hint = "Divide el cambio de entalpía total por la cantidad de moles de producto formado para obtener el cambio de entalpía por mol."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_cambio_entalpia_por_mol()
