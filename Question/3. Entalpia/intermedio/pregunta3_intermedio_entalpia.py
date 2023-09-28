import svgwrite
import random

def generar_pregunta_calor_fusion_hielo():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para la entalpía de fusión del hielo en kJ/mol
    entalpia_fusion = random.uniform(5, 10)  # Valor aleatorio en kJ/mol

    # Masa de hielo a derretir en gramos
    masa_hielo_gramos = random.uniform(10, 100)  # Valor aleatorio en gramos

    # Convierte la masa de hielo a moles
    moles_hielo = masa_hielo_gramos / 18.01528  # Masa molar del agua en g/mol

    # Calcula el calor requerido para derretir la cantidad especificada de hielo
    calor_requerido = entalpia_fusion * moles_hielo

    # Enunciado de la pregunta
    enunciado = f"Si la entalpía de fusión del hielo es de {entalpia_fusion:.2f} kJ/mol y se derriten {masa_hielo_gramos:.2f} gramos de hielo, ¿cuánto calor se requiere?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {calor_requerido:.2f} kJ"

    # Agrega una pista breve
    hint = "Convierte la masa de hielo a moles y luego utiliza la entalpía de fusión para calcular el calor requerido."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_calor_fusion_hielo()


