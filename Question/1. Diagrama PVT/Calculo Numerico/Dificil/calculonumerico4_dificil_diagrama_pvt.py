import svgwrite
import random

def generar_pregunta_calculo_numerico_nuevo_volumen_expansion_isotermica():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para el volumen inicial (entre 3 y 7 litros), la temperatura inicial (entre 300 y 400 Kelvin) y la presión inicial (entre 2 y 6 atmósferas)
    volumen_inicial_litros = random.uniform(3, 7)
    temperatura_inicial_kelvin = random.uniform(300, 400)
    presion_inicial_atm = random.uniform(2, 6)

    # Calcula el nuevo volumen usando la ley de los gases ideales para procesos isotérmicos: P1 * V1 = P2 * V2
    # Suponemos que la presión inicial es P y la presión final es 1 atmósfera
    nuevo_volumen_litros = (volumen_inicial_litros * presion_inicial_atm) / 1

    # Enunciado de la pregunta
    enunciado = f"Un gas ideal se encuentra en un recipiente de {volumen_inicial_litros:.2f} litros a una temperatura de {temperatura_inicial_kelvin:.2f} K\n y una presión de {presion_inicial_atm:.2f} atmósferas. Si se permite que el gas se expanda isotérmicamente\n hasta que su presión alcance 1 atmósfera, ¿cuál será el nuevo volumen del gas?"

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
respuesta = generar_pregunta_calculo_numerico_nuevo_volumen_expansion_isotermica()
