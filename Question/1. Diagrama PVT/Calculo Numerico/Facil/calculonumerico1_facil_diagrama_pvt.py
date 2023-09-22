import svgwrite

def generar_pregunta_calculo_numerico_stp():
    # Especifica la ruta completa del archivo SVG junto con su nombre de archivo.
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con la ruta del archivo
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Valores estándar de temperatura y presión (STP)
    temperatura_stp_kelvin = 273.15  # 0 grados Celsius en Kelvin
    presion_stp_atm = 1.00  # 1 atmósfera

    # Constante de los gases
    constante_de_los_gases = 0.0821  # Constante de los gases en (L * atm) / (mol * K)

    # Calcula el volumen ocupado por un mol de gas ideal a STP
    volumen_litros_stp = (constante_de_los_gases * temperatura_stp_kelvin) / presion_stp_atm

    # Enunciado de la pregunta
    enunciado = "¿Cuál es el volumen ocupado por un mol de gas ideal a condiciones estándar de \n temperatura y presión (STP)?"

    # Respuesta de la pregunta
    respuesta = f"Respuesta: {volumen_litros_stp:.2f} litros"
    
    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # # Agrega la respuesta como texto
    # dwg.add(dwg.text(respuesta, insert=(20, (y_pos)*1.5), fill='black', font_size='14px', text_anchor='start'))

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    return(respuesta)

# Generar la pregunta de cálculo numérico para STP y guardar en el archivo especificado
generar_pregunta_calculo_numerico_stp()
