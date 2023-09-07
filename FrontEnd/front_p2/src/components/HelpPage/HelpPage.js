import React from 'react';
import './HelpPage.css';

function HelpPage() {
  return (
    <div className="help">
      <h1 className="help-title">Ayuda y Soporte</h1>
      <div className="card">
        <h2 className="card-title">Preguntas Frecuentes</h2>
        <p className="card-text">
          Consulta nuestra sección de Preguntas Frecuentes (FAQ) para encontrar respuestas a las preguntas comunes que los estudiantes suelen tener. Es posible que encuentres la respuesta que buscas aquí.
        </p>
      </div>

      <div className="card">
        <h2 className="card-title">Contacto Directo</h2>
        <p className="card-text">
          Si no encuentras la respuesta a tu pregunta en nuestras FAQs, no dudes en ponerte en contacto con nuestro equipo de soporte. Puedes enviarnos un correo electrónico a support@example.com o llamarnos al número +123456789.
        </p>
      </div>

      <div className="card">
        <h2 className="card-title">Comunidad de Estudiantes</h2>
        <p className="card-text">
          Únete a nuestra comunidad de estudiantes en línea. Aquí, puedes interactuar con otros estudiantes, hacer preguntas, compartir conocimientos y obtener apoyo mutuo en tu viaje de aprendizaje.
        </p>
      </div>

      <p className="help-text">
        Estamos aquí para ayudarte en cada paso del camino. ¡No dudes en contactarnos si necesitas ayuda o tienes alguna pregunta!
      </p>
    </div>
  );
}

export default HelpPage;

