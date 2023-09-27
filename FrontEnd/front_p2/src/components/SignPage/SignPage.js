import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './SignPage.css';
import { createUserWithEmailAndPassword, updateProfile } from 'firebase/auth';
import { auth } from '../../firebase'; // Importa el módulo auth de tu configuración Firebase
import { useNavigate } from 'react-router-dom';
import { ref, set } from 'firebase/database';
import { getDatabase } from 'firebase/database';

function SignPage() {
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const userCredential = await createUserWithEmailAndPassword(
        auth,
        formData.email,
        formData.password
      );

      await updateProfile(userCredential.user, {
        displayName: formData.name,
      });

      // Crear un documento de usuario en Firebase Realtime Database
      const db = getDatabase();
      const userRef = ref(db, 'usuarios/' + userCredential.user.uid);
      set(userRef, {
        nombre: formData.name,
        mail: formData.email,
        nivel: 1,
        puntaje: 0,
        rol: 'alumno',
      });

      console.log('Creación de usuario exitosa!');
      navigate('/');
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
