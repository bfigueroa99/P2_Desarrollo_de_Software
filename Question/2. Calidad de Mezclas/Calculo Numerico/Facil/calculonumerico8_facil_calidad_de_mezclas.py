import svgwrite
import random

def generar_pregunta_volumen_total_mezcla_jugo_naranja_agua():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para los volúmenes de jugo de naranja y agua en litros
    volumen_jugo_naranja_litros = random.uniform(0.5, 2)
    volumen_agua_litros = random.uniform(0.5, 2)

    # Calcula el volumen total de la mezcla
    volumen_total_litros = volumen_jugo_naranja_litros + volumen_agua_litros

    # Enunciado de la pregunta
    enunciado = f"Si mezclas {volumen_jugo_naranja_litros:.2f} litros de jugo de naranja con {volumen_agua_litros:.2f} litros de agua, ¿cuál será el volumen\n total de la mezcla?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {volumen_total_litros:.2f} litros"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_volumen_total_mezcla_jugo_naranja_agua()
