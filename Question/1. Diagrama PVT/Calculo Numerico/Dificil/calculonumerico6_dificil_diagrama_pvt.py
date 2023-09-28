import svgwrite
import random

def generar_pregunta_calculo_numerico_cambio_temperatura_expansion_volumen_constante():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la presión inicial (entre 2 y 4 atmósferas) y la temperatura inicial (entre 200 y 400 Kelvin)
    presion_inicial_atm = random.uniform(2, 4)
    temperatura_inicial_kelvin = random.uniform(200, 400)

    # Suponemos que el trabajo de expansión a volumen constante es adiabático, por lo que utilizamos la relación entre presión y temperatura en una expansión adiabática: P1 * V1^γ / T1 = P2 * V2^γ / T2
    # Suponemos que el volumen inicial es V y la presión final es 1 atmósfera
    # γ es el coeficiente adiabático para gases ideales y su valor es 1.4 para el aire
    coeficiente_adiabatico = 1.4
    nueva_temperatura_kelvin = temperatura_inicial_kelvin * (1 / (presion_inicial_atm / 1) ** (1 / coeficiente_adiabatico))

    # Calcula el cambio en la temperatura
    cambio_temperatura_kelvin = temperatura_inicial_kelvin - nueva_temperatura_kelvin

    # Enunciado de la pregunta
    enunciado = f"Un gas ideal se encuentra a una presión de {presion_inicial_atm:.2f} atmósferas y una temperatura de \n{temperatura_inicial_kelvin:.2f} K. Si se realiza un trabajo de expansión a volumen constante en el gas, red-\nuciendo su presión a 1 atmósfera, ¿cuál será el cambio en la temperatura del gas?"
    hint = "Puedes utilizar la ley de Charles para resolver este problema. La ley de Charles establece que, a presión constante, el volumen de un gas es directamente proporcional a su temperatura en kelvin: V1/T1 = V2/T2."

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cambio_temperatura_kelvin:.2f} K"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_cambio_temperatura_expansion_volumen_constante()
