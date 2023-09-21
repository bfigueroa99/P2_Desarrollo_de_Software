import svgwrite
import random

# RESPUESTA: B. Inversamente proporcional

def generar_alternativa1_facil_diagrama_pvt():

    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/alternativa1_facil_diagrama_pvt.svg'

    # Crear un lienzo SVG
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('500px', '500px'))

    # relacion = (random.randint(10,25))
    # # Genera un Diagrama de PVT directamente proporcional
    # puntos_datos = [(x / relacion, x) for x in range(11)]  # Directamente proporcional (y = x)

    # # Escala las coordenadas a las dimensiones del lienzo
    # puntos_escalados = [(p[0] * 280 + 50, p[1] * 280 / 10 + 50) for p in puntos_datos]

    # # Dibuja los puntos en el gráfico
    # for x, y in puntos_escalados:
    #     dwg.add(dwg.circle(center=(x, y), r=3, fill='blue'))


    # # Agrega ejes y etiquetas
    # dwg.add(dwg.line(start=(50, 330), end=(330, 330), stroke=svgwrite.rgb(0, 0, 0, '%')))
    # dwg.add(dwg.line(start=(50, 330), end=(50, 50), stroke=svgwrite.rgb(0, 0, 0, '%')))
    # dwg.add(dwg.text('Volumen', insert=(190, 380), fill='black', font_size='12px', text_anchor='middle'))
    # dwg.add(dwg.text('Presión', insert=(25, 190), fill='black', font_size='12px', text_anchor='middle', transform='rotate(-90,25,190)'))


    # Agrega el enunciado y las alternativas como elementos de texto
    enunciado = "¿Cuál es la relación entre la presión y el volumen en este diagrama?"
    # Agrega las alternativas
    alternativas = ["A. Directamente proporcional", "B. Inversamente proporcional", "C. No hay relación",
                    "D. Relación lineal", "E. Relación exponencial"]
    

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(50, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

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
generar_alternativa1_facil_diagrama_pvt()
