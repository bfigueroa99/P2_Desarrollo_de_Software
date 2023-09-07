import React, { useState } from 'react';
import './LoginPage.css';
import { signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../../firebase';
import { useNavigate } from 'react-router-dom'; // Importa useHistory

function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const navigate = useNavigate(); // Obtiene el objeto de historial

  const handleLogin = async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      console.log("logeado con éxito")
      navigate('/'); // Redirige al usuario a la página de inicio ("/")
    } catch (error) {
      console.log("logeado sin éxito")
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
          ¿No tienes una cuenta? <a href="#">Regístrate aquí</a>
        </p>
      </div>
    </div>
  );
}

export default LoginPage;
