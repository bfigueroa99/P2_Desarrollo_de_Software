import React, { useState, useEffect } from 'react';
import './LoginPage.css';
import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../../firebase';
import { useNavigate } from 'react-router-dom';

function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const unsubscribe = auth.onAuthStateChanged((user) => {
      if (user) {
        // El usuario está autenticado, redirige a la página principal u otra página
        navigate('/');
      }
      // Si no hay usuario autenticado, no se hace nada
    });

    // Limpia el observador cuando el componente se desmonta
    return () => unsubscribe();
  }, [navigate]);

  const handleLogin = async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      console.log("logeado con éxito");
      
      // El usuario será redirigido automáticamente después del inicio de sesión
    } catch (error) {
      console.log("logeado sin éxito");
      setError(error.message);
    }
  };


  return (
    <div className="login-page">
      <h1>Iniciar Sesión</h1>
      <div className="form-container">
        <div className="form-group">
          <label>Correo Electrónico</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Contraseña</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        {error && <p className="error">{error}</p>}
        <button className="login-button" onClick={handleLogin}>
          Iniciar Sesión
        </button>
        <p>
          ¿No tienes una cuenta? <a href="/signup">Regístrate aquí</a>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;
