import svgwrite
import random

def generar_pregunta_preparacion_solucion_diluida():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la concentración original, el volumen deseado y la concentración deseada
    concentracion_original = random.uniform(10, 50)  # Concentración en %
    volumen_deseado_ml = random.uniform(100, 1000)  # Volumen deseado en ml
    concentracion_deseada = random.uniform(5, 20)   # Concentración deseada en %

    # Calcula la cantidad de la solución original requerida
    cantidad_original_ml = (volumen_deseado_ml * concentracion_deseada) / concentracion_original

    # Calcula la cantidad de agua requerida para diluir la solución
    cantidad_agua_ml = volumen_deseado_ml - cantidad_original_ml

    # Enunciado de la pregunta
    enunciado = f"Tienes una solución de ácido clorhídrico con una concentración del {concentracion_original:.2f}%. Si necesi-\ntas preparar {volumen_deseado_ml:.2f} ml de una solución al {concentracion_deseada:.2f}%, ¿cuántos ml de la solución original\n debes usar y cuántos ml de agua necesitas agregar?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Debes usar {cantidad_original_ml:.2f} ml de la solución original y agregar {cantidad_agua_ml:.2f} ml de agua."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_preparacion_solucion_diluida()
