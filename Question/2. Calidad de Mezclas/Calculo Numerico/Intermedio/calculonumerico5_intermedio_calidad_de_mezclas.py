import svgwrite
import random

def generar_pregunta_dilucion_solucion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Concentración de la solución original (en %)
    concentracion_original = 15

    # Cantidad de la solución original en ml
    cantidad_original_ml = random.uniform(100, 500)

    # Concentración deseada de la solución diluida (en %)
    concentracion_deseada = 5

    # Cantidad deseada de la solución diluida en ml
    cantidad_deseada_ml = 400

    # Calcula la cantidad de agua a agregar para diluir la solución original
    cantidad_agua_a_agregar_ml = (cantidad_original_ml * (concentracion_original / concentracion_deseada)) - cantidad_deseada_ml

    # Enunciado de la pregunta
    enunciado = f"Tienes una solución de sal con una concentración del {concentracion_original}% y deseas preparar 400 ml \nde una solución al {concentracion_deseada}%. ¿Cuántos mililitros de agua necesitas agregar a la solución \noriginal?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Necesitas agregar {cantidad_agua_a_agregar_ml:.2f} ml de agua."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_dilucion_solucion()
