import svgwrite
import random

def generar_pregunta_dilucion_solucion_azucar():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Volumen inicial de la solución de azúcar en litros
    volumen_inicial_litros = 3

    # Concentración inicial de azúcar en la solución (variables aleatorias)
    concentracion_inicial = random.randint(10, 30)

    # Volumen deseado de la nueva solución en litros
    volumen_deseado_litros = 5

    # Concentración deseada de azúcar en la nueva solución (10%)
    concentracion_deseada = 10

    # Calcula la cantidad de solución de azúcar que se necesita diluir con agua
    cantidad_diluir_litros = (volumen_deseado_litros * concentracion_deseada) / concentracion_inicial - volumen_deseado_litros

    # Enunciado de la pregunta
    enunciado = f"Tienes {volumen_inicial_litros} litros de una solución de azúcar al {concentracion_inicial}%. ¿Cuántos litros de esta solución nece-\nsitas diluir con agua para obtener {volumen_deseado_litros} litros de una solución al {concentracion_deseada}% de azúcar?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Necesitas diluir {cantidad_diluir_litros:.2f} litros de la solución inicial con agua."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_dilucion_solucion_azucar()
