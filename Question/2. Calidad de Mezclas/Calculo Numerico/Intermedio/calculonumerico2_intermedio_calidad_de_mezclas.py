import svgwrite
import random

def generar_pregunta_aumentar_concentracion_alcohol():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen de la mezcla y la concentración inicial de alcohol
    volumen_mezcla_litros = random.uniform(1, 5)  # Volumen de la mezcla en litros
    concentracion_inicial_alcohol = random.uniform(10, 50)  # Concentración inicial de alcohol en %

    # Calcula la cantidad de alcohol en la mezcla original
    cantidad_alcohol_original_litros = (concentracion_inicial_alcohol / 100) * volumen_mezcla_litros

    # Genera un valor aleatorio para la concentración deseada de alcohol
    concentracion_deseada_alcohol = random.uniform(concentracion_inicial_alcohol + 1, 90)

    # Calcula la cantidad de alcohol que se debe agregar para alcanzar la concentración deseada
    cantidad_alcohol_agregar_litros = ((concentracion_deseada_alcohol / 100) * volumen_mezcla_litros) - cantidad_alcohol_original_litros

    # Enunciado de la pregunta
    enunciado = f"Tienes {volumen_mezcla_litros:.2f} litros de una mezcla de alcohol al {concentracion_inicial_alcohol:.2f}% y agua. Si deseas aumentar la\n concentración de alcohol al {concentracion_deseada_alcohol:.2f}%, ¿cuántos mililitros de alcohol puro debes agr-\negar a la mezcla?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula y formatea la respuesta
    respuesta = f"Respuesta: Debes agregar {cantidad_alcohol_agregar_litros * 1000:.2f} ml de alcohol puro."

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_aumentar_concentracion_alcohol()
