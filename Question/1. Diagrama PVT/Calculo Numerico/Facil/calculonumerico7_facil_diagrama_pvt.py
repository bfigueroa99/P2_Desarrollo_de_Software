import svgwrite
import random

def generar_pregunta_calculo_numerico_moles_gas_ideal():
    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/calculonumerico7_facil_diagrama_pvt.svg'

    # Crea un lienzo SVG con la ruta del archivo
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen (entre 10 y 50 litros), la temperatura (entre 300 y 500 Kelvin) y la presión (entre 1 y 5 atmósferas)
    volumen_litros = random.uniform(10, 50)
    temperatura_kelvin = random.uniform(300, 500)
    presion_atm = random.uniform(1, 5)

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula la cantidad de moles usando la ecuación de los gases ideales: n = (P * V) / (R * T)
    moles = (presion_atm * volumen_litros) / (constante_de_los_gases * temperatura_kelvin)

    # Enunciado de la pregunta
    enunciado = f"Un gas ideal ocupa un volumen de {volumen_litros:.2f} litros a una temperatura de {temperatura_kelvin:.2f} K y una \n presión de {presion_atm:.2f} atmósferas. ¿Cuántos moles de gas hay en el recipiente?"

    # Respuesta de la pregunta
    respuesta = f"Respuesta: {moles:.2f} moles"

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

# Generar la pregunta de cálculo numérico para la cantidad de moles en un gas ideal y guardar en el archivo especificado
generar_pregunta_calculo_numerico_moles_gas_ideal()
