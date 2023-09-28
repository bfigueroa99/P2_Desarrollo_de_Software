import svgwrite
import random

def generar_pregunta_calidad_mezclas_dificil_2():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Porcentaje de azúcar en la primera solución
    porcentaje_azucar_solucion1 = random.uniform(15, 20)  # Valor aleatorio en %

    # Volumen de la primera solución en litros
    volumen_solucion1_litros = random.uniform(0.2, 0.6)  # Valor aleatorio en litros

    # Porcentaje de azúcar en la segunda solución
    porcentaje_azucar_solucion2 = random.uniform(30, 40)  # Valor aleatorio en %

    # Volumen de la segunda solución en litros
    volumen_solucion2_litros = random.uniform(0.4, 0.8)  # Valor aleatorio en litros

    # Calcula el porcentaje de azúcar en la mezcla final
    porcentaje_azucar_final = ((porcentaje_azucar_solucion1 * volumen_solucion1_litros) +
                                (porcentaje_azucar_solucion2 * volumen_solucion2_litros)) / (
                                           volumen_solucion1_litros + volumen_solucion2_litros)

    # Enunciado de la pregunta
    enunciado = f"Si se mezclan {volumen_solucion1_litros:.2f} litros de una solución con {porcentaje_azucar_solucion1:.2f}% de azúcar y {volumen_solucion2_litros:.2f} litros de otra solución con {porcentaje_azucar_solucion2:.2f}% de azúcar, ¿cuál será el porcentaje de azúcar en la mezcla final?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {porcentaje_azucar_final:.2f}%"

    # Agrega una pista breve
    hint = "Utiliza el método de mezcla de soluciones para calcular el porcentaje de azúcar en la mezcla final."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_calidad_mezclas_dificil_2()

