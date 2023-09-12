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
  const [preguntasIncorrectas, setPreguntasIncorrectas] = useState([]); // Nueva lista para preguntas incorrectas
  const [segundaOportunidad, setSegundaOportunidad] = useState(false); // Nuevo estado para controlar la segunda oportunidad

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
          // Respuesta correcta: avanza a la siguiente pregunta y aumenta el contador de respuestas correctas
          setCurrentQuestionIndex(currentQuestionIndex + 1);
          setRespuestaUsuario('');
          setShowHint(false);
          setMensajeError('');
          setRespuestasCorrectas(respuestasCorrectas + 1);
        } else {
          // Respuesta incorrecta en la primera oportunidad: agrega la pregunta a la lista de preguntas incorrectas
          setPreguntasIncorrectas([...preguntasIncorrectas, question]);
          setCurrentQuestionIndex(currentQuestionIndex + 1);
          setRespuestaUsuario('');
          setShowHint(false);
          setMensajeError('');
          setRespuestasIncorrectas(respuestasIncorrectas + 1);
        }
      } else {
        // Verificar respuesta para preguntas de desarrollo
        const respuestaNumerica = parseFloat(respuestaUsuario);
        const respuestaEsperadaNumerica = parseFloat(question.respuesta);

        if (!isNaN(respuestaNumerica) && !isNaN(respuestaEsperadaNumerica)) {
          // Verificar si las partes enteras coinciden
          if (Math.floor(respuestaNumerica) === Math.floor(respuestaEsperadaNumerica)) {
            // Respuesta correcta: avanza automáticamente a la siguiente pregunta y aumenta el contador de respuestas correctas
            setCurrentQuestionIndex(currentQuestionIndex + 1);
            setRespuestaUsuario('');
            setShowHint(false);
            setMensajeError('');
            setRespuestasCorrectas(respuestasCorrectas + 1);
          } else {
            // Respuesta incorrecta en la primera oportunidad: agrega la pregunta a la lista de preguntas incorrectas
            setPreguntasIncorrectas([...preguntasIncorrectas, question]);
            setCurrentQuestionIndex(currentQuestionIndex + 1);
            setRespuestaUsuario('');
            setShowHint(false);
            setMensajeError('');
            setRespuestasIncorrectas(respuestasIncorrectas + 1);
          }
        } else {
          // La respuesta del usuario o la respuesta esperada no son números válidos
          setMensajeError('Por favor, ingresa una respuesta numérica válida.');
          setRespuestasIncorrectas(respuestasIncorrectas + 1);
        }
      }

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
      const question = preguntas[currentQuestionIndex];

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
      
      {juegoFinalizado ? ( // Aqui deberia ir conteo print final de correctas incorrectas Mostrar mensaje de juego finalizado y estadísticas de respuestas
        <div>
          <p>Juego finalizado, has respondido todo.</p>
          <p></p>
          <p></p>
        </div>
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
