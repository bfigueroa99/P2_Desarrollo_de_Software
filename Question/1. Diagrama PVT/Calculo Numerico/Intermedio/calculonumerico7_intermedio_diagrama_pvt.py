import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_presion_reduccion_volumen():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la presión inicial (entre 0.5 y 2 atmósferas) y la temperatura inicial (entre 200 y 400 Kelvin)
    presion_inicial_atm = random.uniform(0.5, 2)
    temperatura_inicial_kelvin = random.uniform(200, 400)

    # Calcula la nueva presión usando la ley de los gases ideales: P1 * V1 = P2 * V2
    # Suponemos que el volumen inicial es V y el volumen reducido a la mitad es 0.5 * V
    nueva_presion_atm = presion_inicial_atm * 2

    # Enunciado de la pregunta
    enunciado = f"Un gas ideal se encuentra a una presión de {presion_inicial_atm:.2f} atmósfera y una temperatura de {temperatura_inicial_kelvin:.2f}\n K. Si su volumen se reduce a la mitad mientras la temperatura se mantiene constante, \n¿cuál será la nueva presión del gas?"
    hint = "Puedes utilizar la ley de Boyle-Mariotte para resolver este problema. La ley de Boyle-Mariotte establece que, a temperatura constante, la presión y el volumen de un gas son inversamente proporcionales: P1 * V1 = P2 * V2."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nueva_presion_atm:.2f} atmósfera"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_nueva_presion_reduccion_volumen()
