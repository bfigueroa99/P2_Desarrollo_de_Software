import React, { useState } from 'react';
import './PreguntasPage.css';

function PreguntasPage() {
  const [showHint, setShowHint] = useState(false);

  const handleHintClick = () => {
    setShowHint(true);
  };

  return (
    <div className="questions-page">
      <h1>Preguntas y Respuestas</h1>
      <div className="question-card">
        <h2>Pregunta 1</h2>
        <p>¿Cuál es la respuesta correcta a esta pregunta?</p>
        <ul className="answer-options">
          <li><button className="answer-button">A. Opción 1</button></li>
          <li><button className="answer-button">B. Opción 2</button></li>
          <li><button className="answer-button">C. Opción 3</button></li>
          <li><button className="answer-button">D. Opción 4</button></li>
          <li><button className="answer-button">E. Opción 5</button></li>
        </ul>
        <button className="hint-button" onClick={handleHintClick}>
          Hint
          {showHint && (
            <span className="hint-popup">Hint: Esta es una pista útil para responder la pregunta.</span>
          )}
        </button>
      </div>
    </div>
  );
}

export default PreguntasPage;

