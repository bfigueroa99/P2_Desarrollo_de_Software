import React from 'react';
import './AboutUsPage.css';

function AboutUsPage() {
  return (
    <div className="about-us">
      <h1 className="about-us-title">Sobre Nosotros</h1>
      <div className="card">
        <p className="card-text">
          Bienvenido a nuestro sitio de aprendizaje de Termodinámica. Somos un equipo de apasionados por la termodinámica que está comprometido con ayudarte a aprender los conceptos clave de esta fascinante disciplina.
        </p>
      </div>

      <div className="card">
        <p className="card-text">
          Nuestro objetivo es proporcionarte una experiencia educativa de alta calidad para que puedas comprender y dominar los principios termodinámicos y aplicarlos en situaciones del mundo real.
        </p>
      </div>

      <p className="about-us-text">
        ¡Gracias por unirte a nosotros en este emocionante viaje de aprendizaje!
      </p>
    </div>
  );
}

export default AboutUsPage;

