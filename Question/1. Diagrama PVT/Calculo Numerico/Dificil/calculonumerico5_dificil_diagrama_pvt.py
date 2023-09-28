import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_temperatura_expansion_adiabatica():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la temperatura inicial (entre 300 y 500 Kelvin) y el volumen inicial (entre 5 y 15 litros)
    temperatura_inicial_kelvin = random.uniform(300, 500)
    volumen_inicial_litros = random.uniform(5, 15)

    # Calcula la nueva temperatura usando la relación entre presión y temperatura en una expansión adiabática: P1 * V1^γ / T1 = P2 * V2^γ / T2
    # Suponemos que la presión inicial es P y la presión final es la mitad de P
    # γ es el coeficiente adiabático para gases ideales y su valor es 1.4 para el aire
    coeficiente_adiabatico = 1.4
    nueva_temperatura_kelvin = temperatura_inicial_kelvin * ((1 / 2) ** (1 - 1 / coeficiente_adiabatico))

    # Enunciado de la pregunta
    enunciado = f"Tienes un gas ideal a una temperatura de {temperatura_inicial_kelvin:.2f} K y un volumen de {volumen_inicial_litros:.2f} litros. Si se le\n permite expandirse adiabáticamente hasta que su presión se reduzca a la mitad, ¿cuál\n será su nueva temperatura?"
    hint = "Puedes utilizar la relación adiabática para resolver este problema. La relación adiabática entre la temperatura (T), la presión (P) y el volumen (V) en un proceso adiabático es P1 * V1^(γ-1) = P2 * V2^(γ-1), donde γ es el índice adiabático (para un gas ideal monoatómico, γ ≈ 5/3)."

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
respuesta = generar_pregunta_calculo_numerico_nueva_temperatura_expansion_adiabatica()
