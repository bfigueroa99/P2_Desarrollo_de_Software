import React, { useState, useEffect } from 'react';
import './PreguntasPage.css';

function PreguntasPage() {
  const [showHint, setShowHint] = useState(false);
  const [preguntas, setPreguntas] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [respuestaUsuario, setRespuestaUsuario] = useState('');
  const [mensajeError, setMensajeError] = useState('');
  const [juegoFinalizado, setJuegoFinalizado] = useState(false);
  const [respuestasCorrectas, setRespuestasCorrectas] = useState(0);
  const [respuestasIncorrectas, setRespuestasIncorrectas] = useState(0);
  const [preguntasIncorrectas, setPreguntasIncorrectas] = useState([]);
  const [segundaOportunidad, setSegundaOportunidad] = useState(false);

  useEffect(() => {
    // Realizar la solicitud HTTP para obtener la lista de preguntas al azar
    fetch('http://143.198.98.190:8000/preguntas/')
      .then((response) => response.json())
      .then((data) => setPreguntas(data.slice(0, 5))) // Obtener solo las primeras 5 preguntas
      .catch((error) => {
        console.error('Error al obtener las preguntas:', error);
        setMensajeError('No se pudieron cargar las preguntas. Inténtalo de nuevo más tarde.');
      });
  }, []);

  const currentQuestion = preguntas[currentQuestionIndex];

  const handleHintClick = () => {
    setShowHint(true);
  };

  const handleRespuestaChange = (e) => {
    setRespuestaUsuario(e.target.value);
  };

  const handleVerificarRespuesta = () => {
    if (currentQuestionIndex < preguntas.length) {
      const question = currentQuestion; // Utiliza la variable desestructurada

      // Comprobar si se han respondido todas las preguntas
      if (currentQuestionIndex === preguntas.length - 1) {
        if (segundaOportunidad || preguntasIncorrectas.length === 0) {
          setJuegoFinalizado(true);
        } else {
          setSegundaOportunidad(true);
          setCurrentQuestionIndex(0);
          setRespuestaUsuario('');
          setShowHint(false);
          setMensajeError('');
          setPreguntas(preguntasIncorrectas); // Cargar preguntas incorrectas para la segunda oportunidad
          setPreguntasIncorrectas([]); // Limpiar la lista de preguntas incorrectas
        }
      }
    }
  };

  const handleSeleccionarAlternativa = (alternativa) => {
    if (currentQuestionIndex < preguntas.length) {
      const question = currentQuestion; // Utiliza la variable desestructurada
      if (alternativa === question.respuesta) {
        // Respuesta correcta: avanza a la siguiente pregunta y aumenta el contador de respuestas correctas
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setRespuestaUsuario('');
        setShowHint(false);
        setMensajeError('');
        setRespuestasCorrectas(respuestasCorrectas + 1);

        // Comprobar si se han respondido todas las preguntas
        if (currentQuestionIndex === preguntas.length - 1) {
          if (segundaOportunidad || preguntasIncorrectas.length === 0) {
            setJuegoFinalizado(true);
          } else {
            setSegundaOportunidad(true);
            setCurrentQuestionIndex(0);
            setRespuestaUsuario('');
            setShowHint(false);
            setMensajeError('');
            setPreguntas(preguntasIncorrectas); // Cargar preguntas incorrectas para la segunda oportunidad
            setPreguntasIncorrectas([]); // Limpiar la lista de preguntas incorrectas
          }
        }
      } else {
        // Respuesta incorrecta en la primera oportunidad: agrega la pregunta a la lista de preguntas incorrectas
        setPreguntasIncorrectas([...preguntasIncorrectas, question]);
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setRespuestaUsuario('');
        setShowHint(false);
        setMensajeError('');
        setRespuestasIncorrectas(respuestasIncorrectas + 1);
      }
    }
  };

  return (
    <div className="questions-page">
      <h1>Preguntas y Respuestas</h1>
  
      {preguntas.length > 0 && currentQuestionIndex < preguntas.length ? (
        <div className="question-card">
          <h2>Pregunta {preguntas[currentQuestionIndex].id}</h2>
  
          <p>{preguntas[currentQuestionIndex].enunciado}</p>
          {preguntas[currentQuestionIndex].tipo === 'alternativas' ? (
            <div className="answer-options">
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('1')}>1. {preguntas[currentQuestionIndex].alternativa1}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('2')}>2. {preguntas[currentQuestionIndex].alternativa2}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('3')}>3. {preguntas[currentQuestionIndex].alternativa3}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('4')}>4. {preguntas[currentQuestionIndex].alternativa4}</button>
            </div>
          ) : (
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
        <div>
          <p>Juego finalizado, has respondido todas las preguntas.</p>
          <p>Respuestas correctas: {respuestasCorrectas}</p>
          <p>Respuestas incorrectas: {respuestasIncorrectas}</p>
        </div>
      )}
    </div>
  );
  
  
}

export default PreguntasPage;