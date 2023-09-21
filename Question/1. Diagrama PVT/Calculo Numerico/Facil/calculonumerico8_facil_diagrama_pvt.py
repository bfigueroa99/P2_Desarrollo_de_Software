import svgwrite
import random

def generar_pregunta_calculo_numerico_volumen_gases_ideales():
    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/calculonumerico8_facil_diagrama_pvt.svg'

    # Crea un lienzo SVG con la ruta del archivo
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la presión (entre 0.5 y 2 atmósferas) y la temperatura (entre 200 y 400 Kelvin)
    presion_atm = random.uniform(0.5, 2)
    temperatura_kelvin = random.uniform(200, 400)

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula el volumen usando la ecuación de los gases ideales: V = (n * R * T) / P
    # Suponemos una cantidad de sustancia de 1 mol (n = 1)
    volumen_litros = (constante_de_los_gases * temperatura_kelvin) / presion_atm

    # Enunciado de la pregunta
    enunciado = f"Si tienes un gas a una presión de {presion_atm:.2f} atmósferas y una temperatura de {temperatura_kelvin:.2f} K, ¿cuál \nsería su volumen si cumple con la ley de los gases ideales?"

    # Respuesta de la pregunta
    respuesta = f"Respuesta: {volumen_litros:.2f} litros"

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

# Generar la pregunta de cálculo numérico para el volumen en un gas ideal y guardar en el archivo especificado
generar_pregunta_calculo_numerico_volumen_gases_ideales()
