import svgwrite
import random

def generar_pregunta_proporcion_jugos():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Cantidad de jugo de naranja y jugo de manzana en ml
    cantidad_jugo_naranja_ml = 400
    cantidad_jugo_manzana_ml = 600

    # Proporción deseada de jugo de naranja a jugo de manzana (3:2)
    proporcion_deseada = [3, 2]

    # Calcula la cantidad total de partes en la proporción deseada
    total_partes = sum(proporcion_deseada)

    # Calcula la cantidad de cada jugo necesaria para obtener la proporción deseada
    cantidad_jugo_naranja_deseada_ml = (cantidad_jugo_naranja_ml * proporcion_deseada[0]) / total_partes
    cantidad_jugo_manzana_deseada_ml = (cantidad_jugo_manzana_ml * proporcion_deseada[1]) / total_partes

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de {cantidad_jugo_naranja_ml} ml de jugo de naranja y {cantidad_jugo_manzana_ml} ml de jugo de manzana. Deseas \nobtener una mezcla con una proporción de {proporcion_deseada[0]}:{proporcion_deseada[1]} de jugo de naranja a jugo de manzana. \n¿Cuántos mililitros de cada jugo debes tomar?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Debes tomar {cantidad_jugo_naranja_deseada_ml:.2f} ml de jugo de naranja y {cantidad_jugo_manzana_deseada_ml:.2f} ml de jugo de manzana."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_proporcion_jugos()
