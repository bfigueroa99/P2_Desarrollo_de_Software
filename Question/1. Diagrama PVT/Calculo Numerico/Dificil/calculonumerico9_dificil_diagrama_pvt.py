import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_temperatura_expansion_adiabatica_triplicar_volumen():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la presión inicial (1 atmósfera) y la temperatura inicial (entre 200 y 400 Kelvin)
    temperatura_inicial_kelvin = random.uniform(200, 400)

    # Suponemos que el proceso es adiabático, por lo que utilizamos la relación entre presión y temperatura en una expansión adiabática: P1 * V1^γ / T1 = P2 * V2^γ / T2
    # Suponemos que el volumen inicial es V y el volumen final es 3V
    # γ es el coeficiente adiabático para gases ideales y su valor es 1.4 para el aire
    coeficiente_adiabatico = 1.4
    nueva_temperatura_kelvin = temperatura_inicial_kelvin * ((1 / 3) ** (1 - 1 / coeficiente_adiabatico))

    # Enunciado de la pregunta
    enunciado = f"Un gas ideal se encuentra a una presión de 1 atmósfera y una temperatura de {temperatura_inicial_kelvin:.2f} K.\n Si se le permite expandirse adiabáticamente hasta que su volumen se triplique, ¿cuál \nserá la nueva temperatura del gas?"

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
respuesta = generar_pregunta_calculo_numerico_nueva_temperatura_expansion_adiabatica_triplicar_volumen()
