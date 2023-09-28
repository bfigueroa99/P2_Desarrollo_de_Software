import svgwrite
import random

def generar_pregunta_tabla_saturacion_dificil_2():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para temperatura y fracción molar
    temperatura = random.randint(0, 100)
    fraccion_molar = random.uniform(0, 1)  # Valor ficticio de la fracción molar

    # Calcula la presión utilizando una tabla de saturación ficticia
    presion = random.uniform(1, 100)  # Valor ficticio en kPa

    # Enunciado de la pregunta
    enunciado = f"A {temperatura}°C y con una fracción molar de vapor de agua de {fraccion_molar:.4f}, ¿cuál es la presión de saturación en kPa a estas condiciones?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta utilizando una tabla de saturación ficticia
    respuesta = random.uniform(1, 100)  # Valor ficticio en kPa

    # Agrega una pista breve
    hint = "La presión de saturación depende de la temperatura y la fracción molar del vapor. Utiliza la fórmula adecuada."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_tabla_saturacion_dificil_2()

