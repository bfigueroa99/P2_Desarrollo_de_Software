import svgwrite
import random

def generar_pregunta_cantidad_de_sal_en_solucion():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera un valor aleatorio para la concentración de la solución en porcentaje (entre 1% y 20%)
    concentracion_porcentaje = random.uniform(1, 20)

    # Genera un valor aleatorio para el volumen de la solución en mililitros (entre 100 ml y 500 ml)
    volumen_ml = random.uniform(100, 500)

    # Calcula la cantidad de sal en gramos en la solución
    cantidad_sal_gramos = (concentracion_porcentaje / 100) * volumen_ml

    # Enunciado de la pregunta
    enunciado = f"Tienes una solución de sal con una concentración del {concentracion_porcentaje}%." \
                f" Si tienes \n{volumen_ml:.2f} ml de esta solución, ¿cuántos gramos de sal contiene?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {cantidad_sal_gramos:.2f} gramos"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_cantidad_de_sal_en_solucion()
