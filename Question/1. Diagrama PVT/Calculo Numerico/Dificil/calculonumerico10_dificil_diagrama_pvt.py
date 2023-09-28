import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_presion_compresion_isotermica():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valores fijos de temperatura inicial (400 K) y volumen inicial (15 litros)
    temperatura_inicial_kelvin = 400
    volumen_inicial_litros = 15

    # Suponemos que el proceso es isotérmico, por lo que utilizamos la ley de los gases ideales: P1 * V1 = P2 * V2
    # Suponemos que el volumen final es la mitad del inicial (V / 2)
    nueva_presion_atm = 1 * volumen_inicial_litros / (volumen_inicial_litros / 2)

    # Enunciado de la pregunta
    enunciado = f"Tienes un gas ideal a una temperatura de {temperatura_inicial_kelvin} K y un volumen de {volumen_inicial_litros} litros. Si se reali-\nza un trabajo de compresión isotérmica en el gas, reduciendo su volumen a la mitad,\n ¿cuál será la nueva presión del gas?"
    hint = "Puedes utilizar la ley de Boyle-Mariotte para resolver este problema. La ley de Boyle-Mariotte establece que, a temperatura constante, la presión y el volumen de un gas son inversamente proporcionales: P1 * V1 = P2 * V2."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nueva_presion_atm} atmósferas"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_nueva_presion_compresion_isotermica()
