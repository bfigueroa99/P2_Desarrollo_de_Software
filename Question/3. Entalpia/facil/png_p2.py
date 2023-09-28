import cairo
from calculonumerico2_facil_entalpia import entalpia_vaporizacion_X

#Create an SVG surface
surface = cairo.SVGSurface("vaso.svg", 600, 650)

#Add context to the surface
context = cairo.Context(surface)

# Configurar 
tamano_letra = 30  # Tamaño de la letra en puntos
context.set_font_size(tamano_letra)
context.set_source_rgb(0.0, 0.0, 0.0)  # Negro

# Dibujar la parte inferior del vaso (con agua)
context.move_to(200, 400) #Izq abajo
context.line_to(300, 400) #Der abajo
context.line_to(335, 250) #Der arriba
context.line_to(165, 250) #Izq arriba
context.close_path()  # Cierra el camino

# Rellenar la parte inferior del vaso con un color
context.set_source_rgb(0.7, 0.4, 0.0)  #Naranjo
context.fill()  # Rellena la parte inferior del vaso
context.set_source_rgb(0.0, 0.0, 0.0)  # Negro
context.set_line_width(2)  # Ancho de línea
context.stroke()  # Dibuja la línea

# Dibujar la parte superior del vaso (sin rellenar)
context.move_to(350, 200)
context.line_to(335, 250)  
context.line_to(165, 250) 
context.line_to(150, 200)
context.close_path()  # Cierra el camino

# Dibujar una línea en la mitad del vaso (sin rellenar)
context.set_source_rgb(0.0, 0.0, 0.0)  # Negro
context.set_line_width(0.5)  # Ancho de línea
context.stroke()  # Dibuja la línea

context.move_to(10, 580)
context.show_text(f" Entalpia vaporizacion= {entalpia_vaporizacion_X} jk/mol")


surface.write_to_png("pds_foto.png")

# Guarda el archivo SVG
surface.finish()
