import svgwrite
import random

def generar_pregunta_reaccion_entalpia_entropia():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para el cambio de Gibbs de la reacción en kJ
    cambio_gibbs = random.uniform(-200, 200)  # Valor aleatorio en kJ

    # Valor aleatorio para la temperatura en grados Celsius
    temperatura_celsius = random.uniform(0, 100)  # Valor aleatorio en °C

    # Calcula el cambio de entalpía de la reacción a partir del cambio de Gibbs y la temperatura
    cambio_entalpia = cambio_gibbs + (273.15 * cambio_entropia / 1000)

    # Enunciado de la pregunta
    enunciado = f"Si el cambio de Gibbs de una reacción es {cambio_gibbs:.2f} kJ y la temperatura es {temperatura_celsius:.2f}°C, ¿cuál es el cambio de entalpía de la reacción en kJ?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cambio_entalpia:.2f} kJ"

    # Agrega una pista breve
    hint = "Utiliza la ecuación de Gibbs: ΔG = ΔH - TΔS para calcular el cambio de entalpía."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_reaccion_entalpia_entropia()

