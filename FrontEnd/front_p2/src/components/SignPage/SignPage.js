import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './SignPage.css';
import { createUserWithEmailAndPassword } from 'firebase/auth'; // Importa la función de registro de Firebase
import { auth } from '../../firebase';

function SignPage() {
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault(); // Evita que el formulario se envíe automáticamente

    try {
      await createUserWithEmailAndPassword(auth, formData.email, formData.password); // Registro con Firebase
      console.log('Creacion de usuario exitosa!')
    } catch (error) {
      setErrors({ ...errors, general: error.message });
    }
  };

  return (
    <div className="sign-up-page">
      <h1>Regístrate</h1>
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Nombre:</label>
            <input
              type="text"
              id="name"
              name="name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              required
            />
            {errors.name && <p className="error">{errors.name}</p>}
          </div>
          <div className="form-group">
            <label htmlFor="email">Correo Electrónico:</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              required
            />
            {errors.email && <p className="error">{errors.email}</p>}
          </div>
          <div className="form-group">
            <label htmlFor="password">Contraseña:</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              required
            />
            {errors.password && <p className="error">{errors.password}</p>}
          </div>
          <button className="signup-button" type="submit">
            Registrarse
          </button>
        </form>
      </div>
      <p>
        ¿Ya tienes una cuenta? <Link to="/login">Inicia sesión aquí</Link>
      </p>
    </div>
  );
}

export default SignPage;
