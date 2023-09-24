import cairo
import random
from calculonumerico2_facil_calidad_de_mezclas import  masa_azucar_gramos, masa_harina_gramos

# Create an SVG surface
surface = cairo.SVGSurface("monton_azucar.svg", 600, 650)

# Add context to the surface
context = cairo.Context(surface)

#Configurar 
tamano_letra = 30  # Tamaño de la letra en puntos
context.set_font_size(tamano_letra)

#Configurar el color
context.set_source_rgb(0.0, 0.0, 0.0)  # Negro

#Dibuja un montón
num_granos = 500
width, height = 600, 500
radio_grano = 5

for _ in range(num_granos):
    x = random.uniform(0, width)
    y = random.uniform(300, height)  # Limitar la altura para que parezca un montón
    context.arc(x, y, radio_grano, 0, 2 * 3.14159265359)  # Dibuja un círculo en posición aleatoria
    context.fill()  # Rellena el círculo

context.move_to(10, 580)
context.show_text(f"Masa azúcar = {masa_azucar_gramos:.2f} g")
context.move_to(10, 620)
context.show_text(f"Masa harina = {masa_harina_gramos:.2f} g")

# Guarda el archivo SVG
surface.finish()
