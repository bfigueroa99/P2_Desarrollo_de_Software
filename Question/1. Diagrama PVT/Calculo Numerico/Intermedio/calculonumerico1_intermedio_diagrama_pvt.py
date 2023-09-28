import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_temperatura():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la temperatura (entre 300 y 500 Kelvin)
    temperatura_actual = random.uniform(300, 500)

    # Calcula la nueva temperatura después de reducir el volumen a la mitad a presión constante
    nueva_temperatura = temperatura_actual / 2

    # Enunciado de la pregunta
    enunciado = f"Un recipiente contiene 3 moles de gas a una temperatura de {temperatura_actual:.2f} K. Si el volumen del\n recipiente se reduce a la mitad mientras la presión se mantiene constante, ¿cuál será la\n nueva temperatura del gas?"
    hint = "Puedes utilizar la ley de Charles para resolver este problema. La ley de Charles establece que, a presión constante, el volumen de un gas es directamente proporcional a su temperatura en kelvin: V1/T1 = V2/T2."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nueva_temperatura:.2f} K"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
generar_pregunta_calculo_numerico_nueva_temperatura()
