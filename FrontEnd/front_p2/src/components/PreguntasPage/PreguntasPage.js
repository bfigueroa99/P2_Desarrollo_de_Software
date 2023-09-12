import React, { useState, useEffect } from 'react';
import './PreguntasPage.css';

function PreguntasPage() {
  const [showHint, setShowHint] = useState(false);
  const [preguntas, setPreguntas] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [respuestaUsuario, setRespuestaUsuario] = useState('');
  const [mensajeError, setMensajeError] = useState('');
  const [juegoFinalizado, setJuegoFinalizado] = useState(false); // Nuevo estado

  useEffect(() => {
    // Realizar la solicitud HTTP para obtener la lista de preguntas al azar
    fetch('http://localhost:8000/api/get_random_question/')
      .then((response) => response.json())
      .then((data) => setPreguntas(data))
      .catch((error) => console.error('Error al obtener las preguntas:', error));
  }, []);

  const handleHintClick = () => {
    setShowHint(true);
  };

  const handleRespuestaChange = (e) => {
    setRespuestaUsuario(e.target.value);
  };

  const handleVerificarRespuesta = () => {
    if (currentQuestionIndex < preguntas.length) {
      const question = preguntas[currentQuestionIndex];

      if (question.tipo === 'alternativas') {
        // Verificar respuesta para preguntas de alternativas
        if (respuestaUsuario === question.respuesta) {
          // Respuesta correcta: avanza a la siguiente pregunta
          setCurrentQuestionIndex(currentQuestionIndex + 1);
          setRespuestaUsuario('');
          setShowHint(false);
          setMensajeError('');
        } else {
          // Respuesta incorrecta: mostrar mensaje de error
          setMensajeError('Respuesta incorrecta. Inténtalo de nuevo.');
        }
      } else {
        // Verificar respuesta para preguntas de desarrollo
        const respuestaNumerica = parseFloat(respuestaUsuario);
        const respuestaEsperadaNumerica = parseFloat(question.respuesta);
        
        if (!isNaN(respuestaNumerica) && !isNaN(respuestaEsperadaNumerica)) {
          // Verificar si las partes enteras coinciden
          if (Math.floor(respuestaNumerica) === Math.floor(respuestaEsperadaNumerica)) {
            // Respuesta correcta: avanza automáticamente a la siguiente pregunta
            setCurrentQuestionIndex(currentQuestionIndex + 1);
            setRespuestaUsuario('');
            setShowHint(false);
            setMensajeError('');
          } else {
            // Respuesta incorrecta: mostrar mensaje de error
            setMensajeError('Respuesta incorrecta. Inténtalo de nuevo.');
          }
        } else {
          // La respuesta del usuario o la respuesta esperada no son números válidos
          setMensajeError('Por favor, ingresa una respuesta numérica válida.');
        }
      }

      // Comprobar si se han respondido todas las preguntas
      if (currentQuestionIndex === preguntas.length - 1) {
        setJuegoFinalizado(true);
      }
    }
  };

  const handleSeleccionarAlternativa = (alternativa) => {
    if (currentQuestionIndex < preguntas.length) {
      const question = preguntas[currentQuestionIndex];

      if (alternativa === question.respuesta) {
        // Respuesta correcta: avanza a la siguiente pregunta
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setRespuestaUsuario('');
        setShowHint(false);
        setMensajeError('');

        // Comprobar si se han respondido todas las preguntas
        if (currentQuestionIndex === preguntas.length - 1) {
          setJuegoFinalizado(true);
        }
      } else {
        // Respuesta incorrecta: mostrar mensaje de error
        setMensajeError('Respuesta incorrecta. Inténtalo de nuevo.');
      }
    }
  };

  return (
    <div className="questions-page">
      <h1>Preguntas y Respuestas</h1>
      
      {juegoFinalizado ? ( // Mostrar mensaje de juego finalizado
        <p>Juego finalizado, has respondido todo.</p>
      ) : preguntas.length > 0 ? (
        <div className="question-card">
          <h2>Pregunta {preguntas[currentQuestionIndex].id}</h2>
          
          <p>{preguntas[currentQuestionIndex].enunciado}</p>
          {preguntas[currentQuestionIndex].tipo === 'alternativas' ? (
            // Renderizar opciones de respuesta para preguntas de alternativas
            <div className="answer-options">
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('1')}>1. {preguntas[currentQuestionIndex].alternativa1}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('2')}>2. {preguntas[currentQuestionIndex].alternativa2}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('3')}>3. {preguntas[currentQuestionIndex].alternativa3}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('4')}>4. {preguntas[currentQuestionIndex].alternativa4}</button>
            </div>
          ) : (
            // Renderizar entrada de respuesta para preguntas de desarrollo
            <div className="answer-input">
              <input
                type="text"
                placeholder="Escribe tu respuesta"
                className="answer-field"
                value={respuestaUsuario}
                onChange={handleRespuestaChange}
              />
              <button className="answer-button" onClick={handleVerificarRespuesta}>
                Verificar Respuesta
              </button>
            </div>
          )}
          <button className="hint-button" onClick={handleHintClick}>
            Hint
            {showHint && <span className="hint-popup">{preguntas[currentQuestionIndex].hint}</span>}
          </button>
          {mensajeError && <p className="error-message">{mensajeError}</p>}
        </div>
      ) : (
        // Mostrar un mensaje de carga mientras se obtienen las preguntas
        <p>Cargando preguntas..</p>
      )}
    </div>
  );
}

export default PreguntasPage;
