import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_presion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la cantidad de moles (entre 2 y 6 moles), la temperatura (entre 300 y 400 Kelvin) y la presión inicial (entre 2 y 4 atmósferas)
    moles = random.uniform(2, 6)
    temperatura_kelvin = random.uniform(300, 400)
    presion_inicial_atm = random.uniform(2, 4)

    # Calcula la nueva presión usando la ecuación de los gases ideales: P2 = (n * R * T) / V2
    # Suponemos que el volumen inicial es V y el volumen duplicado es 2V
    nueva_presion_atm = (moles * 0.0821 * temperatura_kelvin) / (2 * presion_inicial_atm)

    # Enunciado de la pregunta
    enunciado = f"Un recipiente contiene {moles:.2f} moles de gas a una temperatura de {temperatura_kelvin:.2f} K y una presión\n de {presion_inicial_atm:.2f} atmósferas. Si se expande para duplicar su volumen, ¿cuál será la nueva presi-\nón del gas?"
    hint = "Puedes utilizar la ley de los gases ideales para resolver este problema. La ley de los gases ideales establece que PV = nRT, donde P es la presión, V es el volumen, n es la cantidad de sustancia (moles), R es la constante de los gases ideales y T es la temperatura en kelvin."

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
respuesta = generar_pregunta_calculo_numerico_nueva_presion()
