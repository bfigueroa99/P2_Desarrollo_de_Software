import svgwrite
import random

def generar_pregunta_tabla_saturacion_intermedio_3():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para presión y densidad del vapor de agua
    presion = random.uniform(1, 100)  # Valor ficticio en kPa
    densidad_vapor = random.uniform(0.001, 10)  # Valor ficticio en kg/m³

    # Calcula la temperatura utilizando una tabla de saturación ficticia
    temperatura = random.randint(0, 100)

    # Enunciado de la pregunta
    enunciado = f"A {presion:.2f} kPa y con una densidad del vapor de agua de {densidad_vapor:.4f} kg/m³, ¿cuál es la temperatura de saturación en °C a estas condiciones?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta utilizando una tabla de saturación ficticia
    respuesta = random.randint(0, 100)  # Valor ficticio en °C

    # Agrega una pista breve
    hint = "La temperatura de saturación depende de la presión y la densidad del vapor. Utiliza la fórmula adecuada."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_tabla_saturacion_intermedio_3()

