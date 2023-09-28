import svgwrite
import random

def generar_pregunta_calor_liberado_reaccion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para la entalpía de formación estándar de la sustancia en kJ/mol
    entalpia_formacion = random.uniform(-100, -10)  # Valor aleatorio en kJ/mol

    # Cantidad de moles consumidos en la reacción
    moles_consumidos = 2

    # Calcula el calor liberado en la reacción
    calor_liberado = entalpia_formacion * moles_consumidos

    # Enunciado de la pregunta
    enunciado = f"Si la entalpía de formación estándar de una sustancia es de {entalpia_formacion:.2f} kJ/mol, y en una reacción se consumen {moles_consumidos} moles de esta sustancia, ¿cuánto calor se libera en la reacción?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {calor_liberado:.2f} kJ"

    # Agrega una pista breve
    hint = "Utiliza la entalpía de formación estándar para calcular el calor liberado."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_calor_liberado_reaccion()

