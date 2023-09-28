import svgwrite
import random

def generar_pregunta_calculo_numerico_cantidad_moles():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la temperatura (entre 200 y 400 Kelvin) y el volumen (entre 10 y 30 litros)
    temperatura_kelvin = random.uniform(200, 400)
    volumen_litros = random.uniform(10, 30)

    # Genera un valor aleatorio para la nueva presión (1 atmósfera)
    nueva_presion_atm = 1

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula la cantidad de moles usando la ley de los gases ideales: n = (P * V) / (R * T)
    cantidad_moles = (nueva_presion_atm * volumen_litros) / (constante_de_los_gases * temperatura_kelvin)

    # Enunciado de la pregunta
    enunciado = f"Tienes un gas a una temperatura de {temperatura_kelvin:.2f} K y un volumen de {volumen_litros:.2f} litros. Si su presi-\nón se reduce a {nueva_presion_atm:.2f} atmósfera, ¿cuántos moles de gas hay en el recipiente si cumple \ncon la ley de los gases ideales?"
    hint = "Puedes utilizar la ley de los gases ideales para resolver este problema. La ley de los gases ideales establece que PV = nRT, donde P es la presión, V es el volumen, n es la cantidad de sustancia (moles), R es la constante de los gases ideales y T es la temperatura en kelvin."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cantidad_moles:.2f} moles"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_cantidad_moles()
