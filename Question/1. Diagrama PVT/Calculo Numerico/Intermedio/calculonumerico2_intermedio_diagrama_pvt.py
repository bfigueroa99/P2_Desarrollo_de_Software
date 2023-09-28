import svgwrite
import random

def generar_pregunta_calculo_numerico_nuevo_volumen():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen inicial (entre 5 y 20 litros) y la temperatura (entre 200 y 400 Kelvin)
    volumen_inicial_litros = random.uniform(5, 20)
    temperatura_kelvin = random.uniform(200, 400)

    # Genera un valor aleatorio para la nueva presión (entre 2 y 8 atmósferas)
    nueva_presion_atm = random.uniform(2, 8)

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula el nuevo volumen usando la ecuación de los gases ideales: V2 = (n * R * T2) / P2
    # Suponemos una cantidad de sustancia de 1 mol (n = 1)
    nuevo_volumen_litros = (constante_de_los_gases * temperatura_kelvin) / nueva_presion_atm

    # Enunciado de la pregunta
    enunciado = f"Un gas ideal ocupa un volumen de {volumen_inicial_litros:.2f} litros a una temperatura de {temperatura_kelvin:.2f} K. Si se co-\nmprime a una presión de {nueva_presion_atm:.2f} atmósferas, ¿cuál será su nuevo volumen?"
    hint = "Puedes utilizar la ley de los gases ideales para resolver este problema. La ley de los gases ideales establece que PV = nRT, donde P es la presión, V es el volumen, n es la cantidad de sustancia (moles), R es la constante de los gases ideales y T es la temperatura en kelvin."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nuevo_volumen_litros:.2f} litros"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
generar_pregunta_calculo_numerico_nuevo_volumen()
