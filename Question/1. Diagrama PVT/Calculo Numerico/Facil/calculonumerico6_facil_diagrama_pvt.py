import svgwrite
import random

def generar_pregunta_calculo_numerico_presion_gases_ideales():
    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'


    # Crea un lienzo SVG con la ruta del archivo
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la cantidad de moles (entre 0.1 y 1 moles), la temperatura (entre 300 y 400 Kelvin) y el volumen (entre 5 y 20 litros)
    moles = random.uniform(0.1, 1)
    temperatura_kelvin = random.uniform(300, 400)
    volumen_litros = random.uniform(5, 20)

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula la presión usando la ecuación de los gases ideales: P = (n * R * T) / V
    presion_atm = (moles * constante_de_los_gases * temperatura_kelvin) / volumen_litros

    # Enunciado de la pregunta
    enunciado = f"Si tienes {moles:.2f} moles de un gas a una temperatura de {temperatura_kelvin:.2f} K y un volumen de {volumen_litros:.2f} litros, ¿cuál sería su presión si cumple con la ley de los gases ideales?"
    hint = "Puedes utilizar la ley de los gases ideales: PV = nRT, donde P es la presión, V es el volumen, n es la cantidad de sustancia (moles), R es la constante de los gases ideales y T es la temperatura en kelvin."


    # Respuesta de la pregunta
    respuesta = f"Respuesta: {presion_atm:.2f} atmósferas"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # # Agrega la respuesta como texto
    # dwg.add(dwg.text(respuesta, insert=(20, 90), fill='black', font_size='14px', text_anchor='start'))

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    return(respuesta)

# Generar la pregunta de cálculo numérico para la presión en un gas ideal y guardar en el archivo especificado
generar_pregunta_calculo_numerico_presion_gases_ideales()
