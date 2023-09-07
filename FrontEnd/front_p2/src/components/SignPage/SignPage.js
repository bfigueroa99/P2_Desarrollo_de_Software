import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './SignPage.css';

function SignPage() {
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Realiza validaciones aquí antes de enviar los datos al servidor
    const validationErrors = {};
    if (!formData.name) {
      validationErrors.name = 'El campo de nombre es obligatorio.';
    }
    if (!formData.email) {
      validationErrors.email = 'El campo de correo electrónico es obligatorio.';
    }
    if (!formData.password) {
      validationErrors.password = 'El campo de contraseña es obligatorio.';
    }
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length === 0) {
      // Envía los datos al servidor si no hay errores de validación
      // Aquí puedes agregar la lógica para el registro
      setSubmitted(true);
    }
  };

  return (
    <div className="sign-up-page">
      <h1>Regístrate</h1>
      <div className="form-container">
        <div className="form-group">
          <label htmlFor="name">Nombre:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
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
            onChange={handleInputChange}
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
            onChange={handleInputChange}
            required
          />
          {errors.password && <p className="error">{errors.password}</p>}
        </div>
        <button className="signup-button" type="submit">
          Registrarse
        </button>
      </div>
      <p>
        ¿Ya tienes una cuenta? <Link to="/login">Inicia sesión aquí</Link>
      </p>
    </div>
  );
}

export default SignPage;
