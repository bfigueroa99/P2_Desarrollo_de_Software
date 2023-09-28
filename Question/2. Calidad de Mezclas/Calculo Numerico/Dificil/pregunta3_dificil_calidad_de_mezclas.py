import svgwrite
import random

def generar_pregunta_calidad_mezclas_dificil_3():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Concentración molar de una solución inicial
    concentracion_inicial = random.uniform(0.1, 0.5)  # Valor aleatorio en mol/L

    # Volumen de la solución inicial en litros
    volumen_inicial_litros = random.uniform(0.2, 0.6)  # Valor aleatorio en litros

    # Concentración molar de otra solución para mezclar
    concentracion_otra_solucion = random.uniform(0.2, 0.7)  # Valor aleatorio en mol/L

    # Volumen de la otra solución en litros
    volumen_otra_solucion_litros = random.uniform(0.3, 0.8)  # Valor aleatorio en litros

    # Calcula la concentración molar de la mezcla final
    concentracion_final = ((concentracion_inicial * volumen_inicial_litros) +
                           (concentracion_otra_solucion * volumen_otra_solucion_litros)) / (
                                  volumen_inicial_litros + volumen_otra_solucion_litros)

    # Enunciado de la pregunta
    enunciado = f"Si se mezclan {volumen_inicial_litros:.2f} litros de una solución con concentración molar de {concentracion_inicial:.2f} mol/L y {volumen_otra_solucion_litros:.2f} litros de otra solución con concentración molar de {concentracion_otra_solucion:.2f} mol/L, ¿cuál será la concentración molar de la mezcla final?"
    hint = "Esta pregunta no tiene hint."
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {concentracion_final:.2f} mol/L"

    # Agrega una pista breve
    hint = "Aplica el principio de conservación de la cantidad de sustancia para calcular la concentración molar."

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta y la pista
    return respuesta, hint

# Llama a la función y guarda la respuesta y la pista
respuesta, hint = generar_pregunta_calidad_mezclas_dificil_3()

