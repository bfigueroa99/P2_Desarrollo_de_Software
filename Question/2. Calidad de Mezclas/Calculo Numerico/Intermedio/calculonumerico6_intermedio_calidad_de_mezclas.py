import svgwrite
import random

def generar_pregunta_concentracion_grasa_en_mezcla():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Cantidad de leche 1 y leche 2 en litros
    cantidad_leche_1_litros = 1
    cantidad_leche_2_litros = 1

    # Concentración de grasa en leche 1 y leche 2 en %
    concentracion_grasa_leche_1 = 2
    concentracion_grasa_leche_2 = 4

    # Calcula la cantidad total de leche en litros
    cantidad_total_litros = cantidad_leche_1_litros + cantidad_leche_2_litros

    # Calcula la cantidad total de grasa en la mezcla
    cantidad_total_grasa = (cantidad_leche_1_litros * concentracion_grasa_leche_1) + (cantidad_leche_2_litros * concentracion_grasa_leche_2)

    # Calcula la concentración de grasa en la mezcla
    concentracion_grasa_mezcla = (cantidad_total_grasa / cantidad_total_litros)

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de {cantidad_leche_1_litros} litro de leche al {concentracion_grasa_leche_1}% de grasa y {cantidad_leche_2_litros} litro de leche al {concentracion_grasa_leche_2}% de grasa. \n¿Cuál es la concentración de grasa en la mezcla resultante?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: La concentración de grasa en la mezcla resultante es {concentracion_grasa_mezcla:.2f}%."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_concentracion_grasa_en_mezcla()
