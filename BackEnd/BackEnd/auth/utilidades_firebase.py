import firebase_admin
from firebase_admin import db

# Inicializa Firebase
firebase_admin.initialize_app()

# Referencia a la base de datos de Firebase
db_ref = db.reference('/')

# Escribir datos en la base de datos
data = {
    'nombre': 'Ejemplo',
    'edad': 25,
    'curso': 'Django con Firebase'
}
db_ref.child('estudiantes').child('ID_DEL_ESTUDIANTE').set(data)

# Leer datos de la base de datos
student_data = db_ref.child('estudiantes').child('ID_DEL_ESTUDIANTE').get()
print("Datos del estudiante:", student_data)
