import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_temperatura_compresion_adiabatica():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la cantidad de moles (entre 1 y 3 moles), la temperatura inicial (entre 200 y 400 Kelvin) y la presión inicial (entre 1 y 3 atmósferas)
    moles = random.uniform(1, 3)
    temperatura_inicial_kelvin = 273  # 273 K
    presion_inicial_atm = random.uniform(1, 3)

    # Calcula la nueva temperatura usando la ley de los gases ideales para procesos adiabáticos: P1 * V1^γ = P2 * V2^γ
    # Suponemos que el volumen inicial es V y el volumen reducido a la mitad es V/2
    # γ es el coeficiente adiabático para gases ideales y su valor es 1.4 para el aire
    coeficiente_adiabatico = 1.4
    nueva_temperatura_kelvin = temperatura_inicial_kelvin * ((presion_inicial_atm * (1 / 2) ** (1 - 1 / coeficiente_adiabatico)) / (moles * presion_inicial_atm)) ** (-1)

    # Enunciado de la pregunta
    enunciado = f"Un recipiente contiene {moles:.2f} moles de gas ideal a una temperatura de {temperatura_inicial_kelvin:.2f} K y una p-\nresión de {presion_inicial_atm:.2f} atmósfera. Si se realiza un trabajo de compresión adiabática en el gas,\n reduciendo su volumen a la mitad, ¿cuál será la nueva temperatura del gas?"
    hint = "Puedes utilizar la ley de los gases ideales y la relación adiabática para resolver este problema. La relación adiabática entre la temperatura (T), la presión (P) y el volumen (V) en un proceso adiabático es P1 * V1^γ = P2 * V2^γ, donde γ es el índice adiabático (para un gas ideal monoatómico, γ ≈ 5/3)."

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
respuesta = generar_pregunta_calculo_numerico_nueva_temperatura_compresion_adiabatica()
