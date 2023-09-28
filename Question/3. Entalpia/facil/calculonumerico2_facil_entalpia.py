import svgwrite
import random

def generar_pregunta_calor_vaporizacion_sustancia():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para X (entalpía molar estándar de vaporización) y Y (cantidad de moles)
    entalpia_vaporizacion_X = random.uniform(100, 500)  # Valor aleatorio de X en kJ/mol
    cantidad_moles_Y = random.uniform(1, 10)  # Valor aleatorio de Y en moles

    # Calcula la cantidad de calor requerida para vaporizar Y moles de la sustancia
    calor_requerido = entalpia_vaporizacion_X * cantidad_moles_Y

    # Enunciado de la pregunta
    enunciado = f"Si una sustancia tiene una entalpía molar estándar de vaporización de {entalpia_vaporizacion_X:.2f} kJ/mol, ¿cuánto calor se requiere para vaporizar {cantidad_moles_Y:.2f} moles de esa sustancia?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {calor_requerido:.2f} kJ"

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return entalpia_vaporizacion_X, respuesta

# Llama a la función y guarda la respuesta
entalpia_vaporizacion_X, respuesta = generar_pregunta_calor_vaporizacion_sustancia()