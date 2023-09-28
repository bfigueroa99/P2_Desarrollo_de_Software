import svgwrite
import random

def generar_pregunta_entropia_entalpia_reaccion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para el cambio de entalpía total en kJ
    cambio_entalpia_total = random.uniform(-500, 500)  # Valor aleatorio en kJ

    # Valor aleatorio para el cambio de entropía total en J/K
    cambio_entropia_total = random.uniform(-1000, 1000)  # Valor aleatorio en J/K

    # Calcula el cambio de Gibbs de la reacción
    cambio_gibbs = cambio_entalpia_total - (273.15 * cambio_entropia_total / 1000)

    # Enunciado de la pregunta
    enunciado = f"Si el cambio de entalpía de una reacción es {cambio_entalpia_total:.2f} kJ y el cambio de entropía es {cambio_entropia_total:.2f} J/K, ¿cuál es el cambio de Gibbs de la reacción a 25°C en kJ?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cambio_gibbs:.2f} kJ"

    # Agrega una pista breve
    hint = "Utiliza la ecuación de Gibbs: ΔG = ΔH - TΔS"

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_entropia_entalpia_reaccion()

