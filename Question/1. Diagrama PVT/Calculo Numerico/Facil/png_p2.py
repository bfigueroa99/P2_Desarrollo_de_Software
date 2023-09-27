import cairo 
import random 
from calculonumerico2_facil_diagrama_pvt import presion_atm, cambio_de_volumen_litros 

# Create an SVG surface
surface = cairo.SVGSurface("gas_expansion.svg", 600, 650)

# Add context to the surface
context = cairo.Context(surface)

# Configurar el radio de los puntos
radio_punto = 3

# Configurar el tamaño de la letra
tamano_letra = 30  # Tamaño de la letra en puntos
context.set_font_size(tamano_letra)

#Configurar el color de los puntos
context.set_source_rgb(0.0, 0.0, 1.0)  #Azul

num_puntos = 500
width, height = 600, 500
for _ in range(num_puntos):
    x = random.uniform(0, width)
    y = random.uniform(0, height)
    context.arc(x, y, radio_punto, 0, 2 * 3.14159265359)  # Dibuja un círculo en la posición aleatoria
    context.fill()  # Rellena el círculo


# Add labels for the initial pressure, temperature, and final pressure
context.move_to(10, 580)
context.show_text(f"La presión es {presion_atm:.2f}")
presion_atm, cambio_de_volumen_litros
context.move_to(10, 620)
context.show_text(f"El cambio de volumen es {cambio_de_volumen_litros:.2f}")


surface.write_to_png("pds_foto.png")

# Save the surface to an SVG file
surface.finish()