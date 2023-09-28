import svgwrite
import random

def generar_pregunta_cantidad_moles_combustion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para la entalpía estándar de combustión en kJ/mol
    entalpia_combustion = random.uniform(-500, -100)  # Valor aleatorio en kJ/mol

    # Cantidad de calor liberado en la reacción en kJ
    calor_liberado = 200  # Valor fijo en kJ

    # Calcula la cantidad de moles que se deben quemar para liberar el calor especificado
    moles_combustion = calor_liberado / entalpia_combustion

    # Enunciado de la pregunta
    enunciado = f"Si la entalpía estándar de combustión de un compuesto es de {entalpia_combustion:.2f} kJ/mol, ¿cuántos moles de ese compuesto se deben quemar para liberar {calor_liberado} kJ de calor?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {moles_combustion:.2f} moles"

    # Agrega una pista breve
    hint = "Usa la entalpía estándar de combustión para calcular la cantidad de moles."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_cantidad_moles_combustion()

