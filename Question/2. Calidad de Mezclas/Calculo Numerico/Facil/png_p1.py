import cairo
from calculonumerico1_facil_calidad_de_mezclas import cantidad_agua_ml, cantidad_jugo_naranja_ml

#Create an SVG surface
surface = cairo.SVGSurface("vaso.svg", 600, 650)

#Add context to the surface
context = cairo.Context(surface)

# Configurar 
tamano_letra = 30  # Tamaño de la letra en puntos
context.set_font_size(tamano_letra)
context.set_source_rgb(0.0, 0.0, 0.0)  # Negro

#Dibujar el vaso
context.move_to(100, 400)
context.line_to(200, 400)
context.line_to(180, 200)
context.line_to(120, 200)
context.close_path()  # Cierra el camino

#Rellenar el vaso con un color
context.set_source_rgb(0.0, 0.0, 1.0)  # Azul
context.fill_preserve()  # Rellena el vaso

#Contorno del vaso
context.set_source_rgb(0.0, 0.0, 0.0)  # Negro
context.set_line_width(3)
context.stroke()

context.move_to(10, 580)
context.show_text(f" Agua = {cantidad_agua_ml:.2f} ml")
context.move_to(10, 620)
context.show_text(f" Jugo = {cantidad_jugo_naranja_ml:.2f} ml")

# Guarda el archivo SVG
surface.finish()
