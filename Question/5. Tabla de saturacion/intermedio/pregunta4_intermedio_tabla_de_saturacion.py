import svgwrite
import random

def generar_pregunta_tabla_saturacion_intermedio():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para temperatura y presión
    temperatura = random.randint(0, 100)
    presion = random.uniform(1, 100)  # Valor ficticio en kPa

    # Calcula la cantidad de vapor de agua utilizando una tabla de saturación ficticia
    cantidad_vapor = random.uniform(0, 10)  # Valor ficticio en g/m³

    # Enunciado de la pregunta
    enunciado = f"A {temperatura}°C y con una presión de {presion:.2f} kPa, la cantidad de vapor de agua saturado es de {cantidad_vapor:.2f} g/m³. ¿Cuál es la fracción molar del vapor de agua a estas condiciones?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta utilizando una tabla de saturación ficticia
    fraccion_molar = cantidad_vapor / (cantidad_vapor + (1000 - cantidad_vapor))  # Conversión de g/m³ a kg/m³
    respuesta = f"Respuesta: {fraccion_molar:.4f}"

    # Agrega una pista breve
    hint = "La fracción molar es la relación de la cantidad de una sustancia respecto al total de moles en la mezcla. Utiliza la fórmula adecuada."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_tabla_saturacion_intermedio()

