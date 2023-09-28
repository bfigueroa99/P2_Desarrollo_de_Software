import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_presion_agregar_moles():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen inicial (entre 5 y 15 litros), la temperatura (entre 300 y 500 Kelvin) y la presión inicial (entre 1 y 3 atmósferas)
    volumen_inicial_litros = random.uniform(5, 15)
    temperatura_kelvin = random.uniform(300, 500)
    presion_inicial_atm = random.uniform(1, 3)

    # Genera un valor aleatorio para la cantidad de moles adicionales (entre 1 y 5 moles)
    moles_adicionales = random.uniform(1, 5)

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula la nueva presión usando la ley de los gases ideales: P1 * V1 / T1 = P2 * V2 / T2
    # Suponemos que la temperatura se mantiene constante, por lo que T1 = T2
    nueva_presion_atm = (presion_inicial_atm * volumen_inicial_litros) / ((volumen_inicial_litros + (moles_adicionales * 22.4)) * temperatura_kelvin)

    # Enunciado de la pregunta
    enunciado = f"Un gas ocupa un volumen de {volumen_inicial_litros:.2f} litros a una temperatura de {temperatura_kelvin:.2f} K y una presión \nde {presion_inicial_atm:.2f} atmósferas. Si se le agregan {moles_adicionales:.2f} moles de gas adicionales manteniendo la te-\nmperatura constante, ¿cuál será la nueva presión del sistema?"
    hint = "Puedes utilizar la ley de los gases ideales para resolver este problema. Recuerda que, a temperatura constante, la relación entre la presión inicial (P1), el volumen inicial (V1) y la presión final (P2) y el volumen final (V2) es P1 * V1 = P2 * V2."

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
respuesta = generar_pregunta_calculo_numerico_nueva_presion_agregar_moles()
