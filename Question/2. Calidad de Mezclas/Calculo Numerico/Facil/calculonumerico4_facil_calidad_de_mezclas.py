import svgwrite
import random

def generar_pregunta_temperatura_final_mezcla_agua():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para las temperaturas del agua en grados Celsius
    temperatura_agua1_celsius = random.uniform(0, 100)
    temperatura_agua2_celsius = random.uniform(0, 100)

    # Calcula la temperatura final de la mezcla utilizando la ley de la conservación de la energía
    temperatura_final_celsius = (2 * temperatura_agua1_celsius + temperatura_agua2_celsius) / 3

    # Enunciado de la pregunta
    enunciado = f"Si mezclas 2 litros de agua a {temperatura_agua1_celsius:.2f}°C con 1 litro de agua a {temperatura_agua2_celsius:.2f}°C, ¿cuál será la temper-\natura final de la mezcla?"
    hint = "Puedes utilizar la ley de la conservación de la energía para resolver este problema. La temperatura final de la mezcla se calcula mediante la ecuación: m1 * c1 * (Tf - T1) = m2 * c2 * (T2 - Tf), donde m1 y m2 son las masas de los cuerpos, c1 y c2 son las capacidades caloríficas específicas y T1 y T2 son las temperaturas iniciales."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {temperatura_final_celsius:.2f}°C"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_temperatura_final_mezcla_agua()
