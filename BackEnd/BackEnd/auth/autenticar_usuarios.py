import firebase_admin
from firebase_admin import auth

# Inicializa Firebase
firebase_admin.initialize_app()

# Autentica al usuario por correo electrónico y contraseña
try:
    user = auth.get_user_by_email("usuario@example.com")
    print("Usuario autenticado:", user.uid)
except auth.AuthError as e:
    print("Error de autenticación:", e)
