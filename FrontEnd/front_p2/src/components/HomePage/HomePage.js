import React from 'react';

function HomePage() {
  return (
    <div className="home-page">
      <div className="home-header">
        <h1>Bienvenido al Curso de Termodinámica</h1>
        <p>¡Explora el fascinante mundo de la termodinámica y domina sus conceptos clave!</p>
      </div>

      <div className="course-overview">
        <h2>¿Qué aprenderás en este curso?</h2>
        <p>En este emocionante viaje de aprendizaje, te sumergirás en los fundamentos de la termodinámica y desarrollarás una comprensión sólida de conceptos esenciales como:</p>
        <ul>
          <li>Diagramas de PVT, PT, VT y PV</li>
          <li>Calidad de mezclas y cómo afecta a las propiedades termodinámicas</li>
          <li>Entalpía y su relación con los procesos de transferencia de calor</li>
          <li>Calor latente y su papel en las transformaciones de fase</li>
          <li>Uso de la tabla de saturación para análisis de vapor y líquido</li>
        </ul>
      </div>

      <div className="course-benefits">
        <h2>Beneficios del Curso</h2>
        <p>Al completar este curso, estarás preparado para enfrentar desafíos en el campo de la termodinámica y aplicarás tu conocimiento para resolver problemas en la vida real. Además, estarás equipado con las habilidades necesarias para:</p>
        <ul>
          <li>Optimizar procesos termodinámicos en diversas industrias</li>
          <li>Comprender y diseñar sistemas de refrigeración y climatización</li>
          <li>Realizar análisis térmicos y termodinámicos en proyectos de ingeniería</li>
          <li>Mejorar tus capacidades analíticas y de resolución de problemas</li>
        </ul>
      </div>

      <div className="get-started">
        <p>¡Prepárate para sumergirte en el emocionante mundo de la termodinámica! ¿Estás listo para empezar?</p>
        <button className="start-button">Comenzar el Curso</button>
      </div>
    </div>
  );
}

export default HomePage;

