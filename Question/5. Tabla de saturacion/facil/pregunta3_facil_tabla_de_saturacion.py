import svgwrite
import random

def generar_pregunta_tabla_saturacion_facil_3():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para presión y cantidad de vapor
    presion = random.uniform(1, 100)  # Valor ficticio en kPa
    cantidad_vapor = random.uniform(0, 10)  # Valor ficticio en g/m³

    # Calcula la temperatura utilizando una tabla de saturación ficticia
    temperatura = random.randint(0, 100)

    # Enunciado de la pregunta
    enunciado = f"A {presion:.2f} kPa, la cantidad de vapor de agua saturado es de {cantidad_vapor:.2f} g/m³. ¿Cuál es la temperatura de saturación en °C a esta presión?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {temperatura}°C"

    # Agrega una pista breve
    hint = "Utiliza la cantidad de vapor de agua saturado a esa presión como referencia para calcular la temperatura de saturación."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_tabla_saturacion_facil_3()

