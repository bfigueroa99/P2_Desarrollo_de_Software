import React, { useState } from 'react';
import './PreguntasAltPage.css';

function PreguntasAltPage() {
  const [showHint, setShowHint] = useState(false);
  const [userAnswer, setUserAnswer] = useState('');

  const handleHintClick = () => {
    setShowHint(true);
  };

  const handleAnswerChange = (e) => {
    setUserAnswer(e.target.value);
  };

  return (
    <div className="questions-alt-page">
      <h1>Preguntas y Respuestas Alternativas</h1>
      <div className="question-card">
        <h2>Pregunta 2</h2>
        <p>¿Cuál es el número correcto para esta pregunta?</p>
        <div className="answer-input">
          <input
            type="number"
            value={userAnswer}
            onChange={handleAnswerChange}
            placeholder="Escribe tu respuesta"
            className="answer-field"
          />
          <button className="hint-button" onClick={handleHintClick}>
            Hint
            {showHint && (
              <span className="hint-popup">Hint: Esta es una pista útil para responder la pregunta.</span>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}

export default PreguntasAltPage;
