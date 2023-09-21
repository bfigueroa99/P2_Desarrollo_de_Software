import svgwrite
import random

def generar_pregunta_calculo_numerico_nuevo_volumen_enfriamiento():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen inicial (entre 5 y 15 litros) y la temperatura inicial (entre 300 y 500 Kelvin)
    volumen_inicial_litros = random.uniform(5, 15)
    temperatura_inicial_kelvin = random.uniform(300, 500)

    # Genera un valor aleatorio para la nueva temperatura más baja (entre 100 y 300 Kelvin)
    temperatura_baja_kelvin = random.uniform(100, 300)

    # Calcula el nuevo volumen usando la ley de los gases ideales: V1 / T1 = V2 / T2
    nuevo_volumen_litros = (volumen_inicial_litros * temperatura_baja_kelvin) / temperatura_inicial_kelvin

    # Enunciado de la pregunta
    enunciado = f"Tienes un gas ideal en un recipiente de {volumen_inicial_litros:.2f} litros a una temperatura de {temperatura_inicial_kelvin:.2f} K. Si el\n gas se enfría a {temperatura_baja_kelvin:.2f} K mientras se mantiene a una presión constante, ¿cuál será el n-\nuevo volumen del gas?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nuevo_volumen_litros:.2f} litros"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_nuevo_volumen_enfriamiento()
