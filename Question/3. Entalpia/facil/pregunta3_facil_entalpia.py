import svgwrite
import random

def generar_pregunta_entalpia_final_sustancia():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para la entalpía inicial de la sustancia
    entalpia_inicial = random.uniform(10, 100)  # Valor aleatorio en kJ

    # Valor aleatorio para la cantidad de calor añadida
    calor_anadido = random.uniform(1, 50)  # Valor aleatorio en kJ

    # Calcula la entalpía final de la sustancia
    entalpia_final = entalpia_inicial + calor_anadido

    # Enunciado de la pregunta
    enunciado = f"Si la entalpía de una sustancia es de {entalpia_inicial:.2f} kJ y se le añaden {calor_anadido:.2f} kJ de calor, ¿cuál es la entalpía final de la sustancia?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {entalpia_final:.2f} kJ"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_entalpia_final_sustancia()
print(respuesta)
