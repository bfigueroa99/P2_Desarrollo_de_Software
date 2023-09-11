import React, { useState, useEffect } from 'react';
import './PreguntasPage.css';

function PreguntasPage() {
  const [showHint, setShowHint] = useState(false);
  const [question, setQuestion] = useState(null);

  useEffect(() => {
    // Realizar la solicitud HTTP para obtener una pregunta al azar
    fetch('http://localhost:8000/api/get_random_question/')
      .then((response) => response.json())
      .then((data) => setQuestion(data))

      .catch((error) => console.error('Error al obtener la pregunta:', error));
  }, []);

  const handleHintClick = () => {
    setShowHint(true);
  };

  return (
    <div className="questions-page">
      <h1>Preguntas y Respuestas</h1>
      
      {question ? (
        <div className="question-card">
          <h2>Pregunta {question.id}</h2>
          
          <p>{question.enunciado}</p>
          {question.tipo === 'alternativas' ? (
            // Renderizar opciones de respuesta para preguntas de alternativas
            <ul className="answer-options">
              <li>
                <button className="answer-button">A. {question.respuesta}</button>
                
              </li>
              <li>
                <button className="answer-button">B. {question.alternativa2}</button>
              </li>
              <li>
                <button className="answer-button">C. {question.alternativa3}</button>
              </li>
              <li>
                <button className="answer-button">D. {question.alternativa4}</button>
              </li>
            </ul>
          ) : (
            // Renderizar entrada de respuesta para preguntas de desarrollo
            <div className="answer-input">
              <input type="text" placeholder="Escribe tu respuesta" className="answer-field" />
            </div>
          )}
          <button className="hint-button" onClick={handleHintClick}>
            Hint
            {showHint && <span className="hint-popup">{question.hint}</span>}
          </button>
        </div>
      ) : (
        // Mostrar un mensaje de carga mientras se obtiene la pregunta
        <p>Cargando pregunta...</p>
      )}
    </div>
  );
}

export default PreguntasPage;
