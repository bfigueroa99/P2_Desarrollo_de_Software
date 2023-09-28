import svgwrite
import random

def generar_pregunta_proporcion_tres_liquidos():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Volumen total de la mezcla en mililitros
    volumen_total_ml = 600

    # Proporción de los tres líquidos X, Y y Z (variables aleatorias)
    proporcion_x = random.randint(1, 5)
    proporcion_y = random.randint(1, 5)
    proporcion_z = random.randint(1, 5)

    # Calcula la cantidad de cada líquido en la mezcla
    cantidad_x_ml = (volumen_total_ml * proporcion_x) / (proporcion_x + proporcion_y + proporcion_z)
    cantidad_y_ml = (volumen_total_ml * proporcion_y) / (proporcion_x + proporcion_y + proporcion_z)
    cantidad_z_ml = (volumen_total_ml * proporcion_z) / (proporcion_x + proporcion_y + proporcion_z)

    # Enunciado de la pregunta
    enunciado = f"Tienes {volumen_total_ml} ml de una mezcla de tres líquidos X, Y y Z en una proporción de {proporcion_x}:{proporcion_y}:{proporcion_z}. ¿Cu-\nántos mililitros de cada líquido tienes en la mezcla?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Tienes {cantidad_x_ml:.2f} ml de líquido X, {cantidad_y_ml:.2f} ml de líquido Y y {cantidad_z_ml:.2f} ml de líquido Z en la mezcla."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_proporcion_tres_liquidos()
