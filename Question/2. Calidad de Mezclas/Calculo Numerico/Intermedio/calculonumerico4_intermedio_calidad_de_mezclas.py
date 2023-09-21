import svgwrite
import random

def generar_pregunta_obtener_lquido_de_mezcla():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera un valor aleatorio para la cantidad total de la mezcla en ml
    cantidad_total_ml = random.uniform(200, 1000)

    # Calcula la cantidad de líquido B en la mezcla original en una proporción de 4:1
    cantidad_liquido_b_original_ml = (1 / 5) * cantidad_total_ml

    # Genera un valor aleatorio para la cantidad deseada de líquido B puro en ml
    cantidad_deseada_liquido_b_puro_ml = random.uniform(50, 300)

    # Calcula la cantidad de la mezcla original que se debe tomar para obtener la cantidad deseada de líquido B puro
    cantidad_mezcla_original_a_tomar_ml = (cantidad_deseada_liquido_b_puro_ml / cantidad_liquido_b_original_ml) * cantidad_total_ml

    # Enunciado de la pregunta
    enunciado = f"Tienes una mezcla de dos líquidos A y B en una proporción de 4:1. Si tienes {cantidad_total_ml:.2f} ml\n de la mezcla y deseas obtener {cantidad_deseada_liquido_b_puro_ml:.2f} ml de líquido B puro, ¿cuántos mililitros de la m-\nezcla original debes tomar?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Debes tomar {cantidad_mezcla_original_a_tomar_ml:.2f} ml de la mezcla original."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_obtener_lquido_de_mezcla()
