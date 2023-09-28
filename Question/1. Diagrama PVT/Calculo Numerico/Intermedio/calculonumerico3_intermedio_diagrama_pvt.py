import svgwrite
import random

def generar_pregunta_calculo_numerico_nuevo_volumen_temperatura():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la presión (entre 1 y 3 atmósferas) y la temperatura inicial (entre 200 y 400 Kelvin)
    presion_inicial_atm = random.uniform(1, 3)
    temperatura_inicial_kelvin = random.uniform(200, 400)

    # Genera un valor aleatorio para la nueva temperatura (entre 300 y 500 Kelvin)
    nueva_temperatura_kelvin = random.uniform(300, 500)

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula el nuevo volumen usando la ecuación de los gases ideales: V2 = (n * R * T2) / P1
    # Suponemos una cantidad de sustancia de 1 mol (n = 1)
    nuevo_volumen_litros = (constante_de_los_gases * nueva_temperatura_kelvin) / presion_inicial_atm

    # Enunciado de la pregunta
    enunciado = f"Tienes un gas a una presión de {presion_inicial_atm:.2f} atmósferas y una temperatura de {temperatura_inicial_kelvin:.2f} K. Si au-\nmentas la temperatura a {nueva_temperatura_kelvin:.2f} K, ¿cuál será el nuevo volumen del gas si cumple con\n la ley de los gases ideales?"
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
generar_pregunta_calculo_numerico_nuevo_volumen_temperatura()
