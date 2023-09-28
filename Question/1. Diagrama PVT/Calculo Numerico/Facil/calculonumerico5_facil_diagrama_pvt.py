import svgwrite
import random

def generar_pregunta_calculo_numerico_temperatura_kelvin():
    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con la ruta del archivo
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen (entre 1 y 10 litros) y la temperatura en grados Celsius (entre -50 y 50 °C)
    volumen_litros = random.uniform(1, 10)
    temperatura_celsius = random.uniform(-50, 50)

    # Calcula la temperatura en Kelvin usando la ecuación de conversión
    temperatura_kelvin = temperatura_celsius + 273.15

    # Enunciado de la pregunta
    hint = "Para convertir la temperatura de grados Celsius a Kelvin, puedes utilizar la siguiente fórmula: Kelvin = Celsius + 273.15."
    enunciado = f"Si tienes un gas ideal con un volumen de {volumen_litros:.2f} litros a {temperatura_celsius:.2f}°C, ¿cuál sería su temperatura en Kelvin?"


    # Respuesta de la pregunta
    respuesta = f"Respuesta: {temperatura_kelvin:.2f} K"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Agrega la respuesta como texto
    # dwg.add(dwg.text(respuesta, insert=(20, 90), fill='black', font_size='14px', text_anchor='start'))

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    return(volumen_litros, temperatura_celsius, respuesta)

# Generar la pregunta de cálculo numérico para la temperatura en Kelvin y guardar en el archivo especificado
volumen_litros, temperatura_celsius = generar_pregunta_calculo_numerico_temperatura_kelvin()
