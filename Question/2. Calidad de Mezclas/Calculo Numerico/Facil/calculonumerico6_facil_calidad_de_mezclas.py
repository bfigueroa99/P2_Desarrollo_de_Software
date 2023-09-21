import svgwrite
import random

def generar_pregunta_volumen_total_mezcla_alcohol_agua():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para los volúmenes de alcohol y agua en mililitros
    volumen_alcohol_ml = random.uniform(50, 300)
    volumen_agua_ml = random.uniform(100, 500)

    # Calcula el volumen total de la mezcla
    volumen_total_ml = volumen_alcohol_ml + volumen_agua_ml

    # Enunciado de la pregunta
    enunciado = f"Si mezclas {volumen_alcohol_ml:.2f} ml de alcohol con {volumen_agua_ml:.2f} ml de agua, ¿cuál es el volumen total de\n la mezcla?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {volumen_total_ml:.2f} ml"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_volumen_total_mezcla_alcohol_agua()
