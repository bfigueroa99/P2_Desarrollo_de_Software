import firebase_admin
from firebase_admin import auth

# Inicializa Firebase
firebase_admin.initialize_app()

# Crea un nuevo usuario
new_user = auth.create_user(
    email="usuario@example.com",
    email_verified=False,
    password="contraseña_secreta",
    display_name="Nombre del Usuario",
    disabled=False
)

# Imprime el UID del usuario recién creado
print("Usuario creado:", new_user.uid)
