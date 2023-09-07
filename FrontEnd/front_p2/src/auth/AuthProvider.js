// AuthProvider.js
import React, { createContext, useContext, useEffect, useState } from 'react';
import { auth } from '../firebase'; // Importa tu instancia de Firebase aquí

// Crea un contexto de autenticación
const AuthContext = createContext();

// Componente AuthProvider que proporciona el contexto
export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Agrega un observador de autenticación de Firebase para manejar cambios en la autenticación
    const unsubscribe = auth.onAuthStateChanged((authUser) => {
      if (authUser) {
        // El usuario está autenticado
        setUser(authUser);
      } else {
        // El usuario no está autenticado
        setUser(null);
      }
    });

    // Limpia el observador cuando el componente se desmonta
    return () => unsubscribe();
  }, []);

  return (
    <AuthContext.Provider value={{ user }}>
      {children}
    </AuthContext.Provider>
  );
}

// Hook personalizado para acceder al contexto de autenticación
export function useAuth() {
  return useContext(AuthContext);
}
