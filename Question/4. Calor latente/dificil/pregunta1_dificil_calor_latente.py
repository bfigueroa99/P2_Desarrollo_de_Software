import svgwrite
import random

def generar_pregunta_calor_latente_dificil_1():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valor aleatorio para el calor latente de vaporización del nitrógeno en J/g
    calor_latente_vaporizacion_nitrogeno = random.uniform(197, 204)  # Valor aleatorio en J/g

    # Masa de nitrógeno a evaporar en gramos
    masa_nitrogeno_gramos = random.uniform(60, 80)  # Valor aleatorio en gramos

    # Calcula el calor requerido para evaporar la cantidad especificada de nitrógeno
    calor_requerido = calor_latente_vaporizacion_nitrogeno * masa_nitrogeno_gramos

    # Enunciado de la pregunta
    enunciado = f"Si el calor latente de vaporización del nitrógeno es de {calor_latente_vaporizacion_nitrogeno:.2f} J/g y se evaporan {masa_nitrogeno_gramos:.2f} gramos de nitrógeno, ¿cuánto calor se requiere?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {calor_requerido:.2f} J"

    # Agrega una pista breve
    hint = "Utiliza el calor latente de vaporización para calcular el calor requerido."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_calor_latente_dificil_1()

