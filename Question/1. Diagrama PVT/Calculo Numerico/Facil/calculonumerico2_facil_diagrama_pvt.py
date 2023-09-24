import svgwrite
import random

def generar_pregunta_calculo_numerico_trabajo_isobarico():
    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'
    # Crea un lienzo SVG con la ruta del archivo
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la presión (entre 1 y 10 atmósferas) y el cambio de volumen (entre 5 y 20 litros)
    presion_atm = random.uniform(1, 10)
    cambio_de_volumen_litros = random.uniform(5, 20)

    # Calcula el trabajo realizado en una expansión isobárica: trabajo = presión * cambio de volumen
    trabajo_atm_litros = presion_atm * cambio_de_volumen_litros

    # Enunciado de la pregunta
    enunciado = f"¿Cuál es el trabajo realizado por un gas en una expansión isobárica si la presión \n es de {presion_atm:.2f} atm y el cambio de volumen es de {cambio_de_volumen_litros:.2f} litros?"

    # Respuesta de la pregunta
    respuesta = f"Respuesta: {trabajo_atm_litros:.2f} atm·L"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    radio_punto = 2

    num_puntos = 300
    width, height = 200, 100
    for _ in range(num_puntos):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        dwg.add(dwg.circle(center=(x, y), r=radio_punto, fill='blue'))

    # # Agrega la respuesta como texto
    # dwg.add(dwg.text(respuesta, insert=(20, 90), fill='black', font_size='14px', text_anchor='start'))

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    return(presion_atm,cambio_de_volumen_litros,respuesta)

# Generar la pregunta de cálculo numérico para trabajo en expansión isobárica y guardar en el archivo especificado
presion_atm, cambio_de_volumen_litros, respuesta = generar_pregunta_calculo_numerico_trabajo_isobarico()


