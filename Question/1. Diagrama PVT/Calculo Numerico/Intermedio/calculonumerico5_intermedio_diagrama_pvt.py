import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_temperatura_compresion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen inicial (entre 10 y 20 litros) y la temperatura inicial (entre 0 y 100°C)
    volumen_inicial_litros = random.uniform(10, 20)
    temperatura_inicial_celsius = random.uniform(0, 100)

    # Genera un valor aleatorio para la nueva presión (entre 1 y 10 atmósferas)
    nueva_presion_atm = random.uniform(1, 10)

    # Convierte la temperatura inicial de Celsius a Kelvin
    temperatura_inicial_kelvin = temperatura_inicial_celsius + 273.15

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula la nueva temperatura usando la ecuación de los gases ideales: T2 = (P2 * V1) / (n * R)
    # Suponemos una cantidad de sustancia de 1 mol (n = 1)
    nueva_temperatura_kelvin = (nueva_presion_atm * volumen_inicial_litros) / (constante_de_los_gases)

    # Enunciado de la pregunta
    enunciado = f"Si tienes un gas ideal con un volumen de {volumen_inicial_litros:.2f} litros a {temperatura_inicial_celsius:.2f}°C y lo comprimes a una p-\nresión de {nueva_presion_atm:.2f} atmósferas, ¿cuál será la nueva temperatura en Kelvin?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nueva_temperatura_kelvin:.2f} K"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_nueva_temperatura_compresion()
