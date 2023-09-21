import svgwrite
import random

def generar_pregunta_calculo_numerico():
    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/calculonumerico1_facil_diagrama_pvt.svg'

    # Crea un lienzo SVG con la ruta del archivo
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera un valor aleatorio para la temperatura en grados Celsius (entre -100 y 100)
    celsius = random.randint(-100, 100)

    # Calcula la temperatura en Kelvin
    kelvin = celsius + 273.15

    # Actualiza el enunciado y la respuesta
    enunciado = f"¿Cuál es la temperatura absoluta en grados Kelvin equivalente a {celsius} grados Celsius?"
    respuesta = f"Respuesta: {kelvin:.2f} K"

    # Agrega el enunciado como texto
    dwg.add(dwg.text(enunciado, insert=(20, 50), fill='black', font_size='14px', text_anchor='start'))

    # Agrega la respuesta como texto
    # dwg.add(dwg.text(respuesta, insert=(20, 90), fill='black', font_size='14px', text_anchor='start'))
    print(respuesta)

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

# Generar la pregunta de cálculo numérico y guardar en el archivo especificado
generar_pregunta_calculo_numerico()
