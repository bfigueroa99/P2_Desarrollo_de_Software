import cairo

# Create an SVG surface
surface = cairo.SVGSurface("gas_expansion.svg", 200, 200)

# Add context to the surface
context = cairo.Context(surface)

presion_inicial_atm = 10
temperatura_kelvin = 100
nueva_presion_atm = 34



# Draw a cylinder with a piston
context.rectangle(50, 50, 100, 100)
context.rectangle(60, 60, 80, 80)
context.stroke()

# Draw arrows indicating the expansion of the gas
context.move_to(70, 70)
context.line_to(70, 30)
context.line_to(130, 30)
context.line_to(130, 70)
context.stroke()

# Add labels for the initial pressure, temperature, and final pressure
context.move_to(10, 120)
context.show_text(f"Initial pressure: {presion_inicial_atm:.2f} atm")
context.move_to(10, 140)
context.show_text(f"Temperature: {temperatura_kelvin:.2f} K")
context.move_to(10, 160)
context.show_text(f"Final pressure: {nueva_presion_atm:.2f} atm")

# Save the surface to an SVG file
surface.finish()