import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_temperatura_calentamiento_presion_constante():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen inicial (entre 5 y 10 litros) y la temperatura inicial (entre 200 y 300 Kelvin)
    volumen_inicial_litros = random.uniform(5, 10)
    temperatura_inicial_kelvin = random.uniform(200, 300)

    # Suponemos que el proceso es a presión constante, por lo que podemos usar la ley de los gases ideales: P1 * V1 / T1 = P2 * V2 / T2
    # Suponemos que el volumen inicial es V y el volumen final es 2V
    nueva_temperatura_kelvin = (temperatura_inicial_kelvin * 1 * 2) / volumen_inicial_litros

    # Enunciado de la pregunta
    enunciado = f"Tienes un gas ideal en un recipiente de {volumen_inicial_litros:.2f} litros a una temperatura de {temperatura_inicial_kelvin:.2f} K. Si el\n gas se calienta a presión constante hasta que su volumen se duplique, ¿cuál será la n-\nueva temperatura del gas?"

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
respuesta = generar_pregunta_calculo_numerico_nueva_temperatura_calentamiento_presion_constante()
