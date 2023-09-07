import React from 'react';
import { Link, NavLink, Outlet, Navigate } from 'react-router-dom';
import './NavBar.css';
import { useAuth } from '../../auth/AuthProvider'; // Importa tu contexto de autenticación aquí
import { getAuth, signOut } from 'firebase/auth'; // Importa el método de cierre de sesión de Firebase

function NavBar() {
  const { user } = useAuth(); // Suponiendo que tu contexto de autenticación proporciona el usuario
  const auth = getAuth(); // Obtén el objeto de autenticación de Firebase

  const signOutUser = async () => {
    try {
      await signOut(auth); // Cierra la sesión del usuario utilizando Firebase Authentication
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
    }
  };

  return (
    <nav className="navbar">
      <Link to="/" className="navbar-brand">
        TermoClass
      </Link>
      <ul className="navbar-nav">
        <li className="nav-item">
          <NavLink to="/about" className="nav-link" activeClassName="active">
            Acerca de
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink to="/help" className="nav-link" activeClassName="active">
            Ayuda
          </NavLink>
        </li>
        {user ? (
          // Si el usuario ha iniciado sesión, muestra su nombre y un botón de cierre de sesión
          <>
            <li className="nav-item">
              <NavLink
                to="/account"
                className="nav-link"
                activeClassName="active"
              >
                {user.displayName} {/* Muestra el nombre del usuario */}
              </NavLink>
            </li>
            <li className="nav-item">
              <button className="nav-link" onClick={signOutUser}>
                Cerrar sesión {/* Botón de cierre de sesión */}
              </button>
            </li>
            {/* Rutas permitidas solo para usuarios autenticados */}
            <li className="nav-item">
              <NavLink to="/account" className="nav-link" activeClassName="active">
                Account
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to="/start" className="nav-link" activeClassName="active">
                Start
              </NavLink>
            </li>
          </>
        ) : (
          // Si el usuario no ha iniciado sesión, muestra enlaces de registro e inicio de sesión
          <>
            
            <li className="nav-item">
              <NavLink
                to="/login"
                className="nav-link"
                activeClassName="active"
              >
                Iniciar sesión
              </NavLink>
            </li>
          </>
        )}
        
      </ul>
    </nav>
  );
}

export default NavBar;
