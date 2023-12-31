import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_presion_triplicar_volumen():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la presión inicial (entre 1 y 3 atmósferas) y la temperatura (entre 200 y 400 Kelvin)
    presion_inicial_atm = random.uniform(1, 3)
    temperatura_kelvin = random.uniform(200, 400)

    # Calcula la nueva presión usando la ley de los gases ideales: P1 * V1 = P2 * V2
    # Suponemos que el volumen inicial es V y el volumen triplicado es 3V
    nueva_presion_atm = presion_inicial_atm / 3

    # Enunciado de la pregunta
    enunciado = f"Un gas ideal se encuentra a una presión de {presion_inicial_atm:.2f} atmósferas y una temperatura de {temperatura_kelvin:.2f}\n K. Si se le permite expandirse isotérmicamente hasta que su volumen se triplique, ¿cu-\nál será la nueva presión del gas?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nueva_presion_atm:.2f} atmósferas"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_nueva_presion_triplicar_volumen()
