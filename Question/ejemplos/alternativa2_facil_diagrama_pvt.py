import svgwrite
import random

# RESPUESTA: A. Directamente proporcional

def generar_alternativa2_facil_diagrama_pvt():

    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/alternativa2_facil_diagrama_pvt.svg'

    # Crear un lienzo SVG
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('500px', '500px'))

     # Agrega el enunciado y las alternativas como elementos de texto
    enunciado = "¿Cuál es la relación entre el volumen y la temperatura en este \n diagrama?"
    alternativas = [
        "A. Directamente proporcional",
        "B. Inversamente proporcional",
        "C. No hay relación",
        "D. Lineal",
        "E. Exponencial"
    ]

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(50, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # x = random.uniform(0.01,0.1)
    # escala_y = random.uniform(2,20)
    #  # Genera puntos de datos aleatorios para el gráfico de volumen y temperatura
    # puntos_datos = [(x + (_ * 0.1),155 - (_ * escala_y)) for _ in range(10)]

    # # Escala las coordenadas a las dimensiones del lienzo
    # puntos_escalados = [(p[0] * 280 + 50, (p[1] - 20) * 2 + 50) for p in puntos_datos]

    # # Dibuja los puntos en el gráfico
    # for x, y in puntos_escalados:
    #     dwg.add(dwg.circle(center=(x, y), r=3, fill='blue'))

    # # Agrega ejes y etiquetas
    # dwg.add(dwg.line(start=(50, 330 + y_pos), end=(330, 330 + y_pos), stroke=svgwrite.rgb(0, 0, 0, '%')))
    # dwg.add(dwg.line(start=(50, 330 + y_pos), end=(50, 50 + y_pos), stroke=svgwrite.rgb(0, 0, 0, '%')))
    # dwg.add(dwg.text('Volumen', insert=(190, 380+y_pos), fill='black', font_size='12px', text_anchor='middle'))
    # dwg.add(dwg.text('Temperatura', insert=(25, 190), fill='black', font_size='12px', text_anchor='middle', transform='rotate(-90,25,190)'))

   

    # Posiciones para las alternativas
    x_alternativa = 50
    y_alternativa = 100
    espacio_entre_alternativas = 20


    # Agrega las alternativas como texto
    for alternativa in alternativas:
        dwg.add(dwg.text(alternativa, insert=(x_alternativa, y_alternativa), fill='black', font_size='12px'))
        y_alternativa += espacio_entre_alternativas

    # Guarda el SVG generado en un archivo
    dwg.save()

# Generar el Diagrama de PVT con la pregunta y guardar en un archivo
generar_alternativa2_facil_diagrama_pvt()
