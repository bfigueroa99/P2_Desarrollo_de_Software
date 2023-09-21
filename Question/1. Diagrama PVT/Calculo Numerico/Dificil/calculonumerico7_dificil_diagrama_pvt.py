import svgwrite
import random

def generar_pregunta_calculo_numerico_nueva_temperatura_cambio_presion_volumen():
    # Ruta simple para el archivo SVG
    ruta_archivo_svg = 'Question/SVG_tmp/tmp.svg'

    # Crea un lienzo SVG con un tamaño ligeramente mayor
    dwg = svgwrite.Drawing(ruta_archivo_svg, profile='tiny', size=('600px', '200px'))

    # Genera valores aleatorios para la cantidad de moles (entre 2 y 4 moles), la temperatura inicial (entre 300 y 400 Kelvin) y la presión inicial (entre 1 y 3 atmósferas)
    moles = random.uniform(2, 4)
    temperatura_inicial_kelvin = random.uniform(300, 400)
    presion_inicial_atm = random.uniform(1, 3)

    # Suponemos que el cambio de presión y volumen se realiza manteniendo constante la cantidad de moles, por lo que podemos usar la ley de los gases ideales: P1 * V1 / T1 = P2 * V2 / T2
    # Suponemos que el volumen inicial es V y el volumen final es 2V
    nueva_temperatura_kelvin = (temperatura_inicial_kelvin * presion_inicial_atm * 2) / (moles * 1)

    # Enunciado de la pregunta
    enunciado = f"Un recipiente contiene {moles:.2f} moles de gas ideal a una temperatura de {temperatura_inicial_kelvin:.2f} K y una p-\nresión de {presion_inicial_atm:.2f} atmósferas. Si se lleva el gas a un estado en el que su presión sea de 1 a-\ntmósfera y su volumen sea el doble del inicial, ¿cuál será la nueva temperatura del gas?"

    # Divide el enunciado en líneas separadas por '\n' y ajusta la posición vertical
    lineas_enunciado = enunciado.split('\n')
    espacio_entre_lineas = 18
    y_pos = 50

    for linea in lineas_enunciado:
        dwg.add(dwg.text(linea, insert=(20, y_pos), fill='black', font_size='14px', text_anchor='start'))
        y_pos += espacio_entre_lineas

    # Calcula la respuesta
    respuesta = f"Respuesta: {nueva_temperatura_kelvin:.2f} K"

    # No agrega la respuesta como texto

    # Guarda el SVG generado en el archivo especificado
    dwg.save()

    # Retorna la respuesta
    return respuesta

# Llama a la función y guarda la respuesta
respuesta = generar_pregunta_calculo_numerico_nueva_temperatura_cambio_presion_volumen()
