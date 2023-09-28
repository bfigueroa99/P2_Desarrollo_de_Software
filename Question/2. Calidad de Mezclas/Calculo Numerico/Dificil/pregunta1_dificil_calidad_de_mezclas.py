import svgwrite
import random

def generar_pregunta_calidad_mezclas_dificil_1():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Porcentaje de alcohol en la primera solución
    porcentaje_alcohol_solucion1 = random.uniform(20, 30)  # Valor aleatorio en %

    # Volumen de la primera solución en litros
    volumen_solucion1_litros = random.uniform(0.1, 0.5)  # Valor aleatorio en litros

    # Porcentaje de alcohol en la segunda solución
    porcentaje_alcohol_solucion2 = random.uniform(60, 70)  # Valor aleatorio en %

    # Volumen de la segunda solución en litros
    volumen_solucion2_litros = random.uniform(0.3, 0.7)  # Valor aleatorio en litros

    # Calcula el porcentaje de alcohol en la mezcla final
    porcentaje_alcohol_final = ((porcentaje_alcohol_solucion1 * volumen_solucion1_litros) +
                                (porcentaje_alcohol_solucion2 * volumen_solucion2_litros)) / (
                                           volumen_solucion1_litros + volumen_solucion2_litros)

    # Enunciado de la pregunta
    enunciado = f"Si se mezclan {volumen_solucion1_litros:.2f} litros de una solución con {porcentaje_alcohol_solucion1:.2f}% de alcohol y {volumen_solucion2_litros:.2f} litros de otra solución con {porcentaje_alcohol_solucion2:.2f}% de alcohol, ¿cuál será el porcentaje de alcohol en la mezcla final?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {porcentaje_alcohol_final:.2f}%"

    # Agrega una pista breve
    hint = "Utiliza el método de mezcla de soluciones para calcular el porcentaje de alcohol en la mezcla final."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_calidad_mezclas_dificil_1()

