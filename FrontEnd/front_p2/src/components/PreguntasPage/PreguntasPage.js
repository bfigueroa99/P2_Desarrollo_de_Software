import React, { useState, useEffect } from 'react';
import './PreguntasPage.css';
import { useAuth } from '../../auth/AuthProvider';
import { getDatabase, ref, push } from 'firebase/database';

const PreguntasPage = () => {
  const { user } = useAuth();
  const [showHint, setShowHint] = useState(false);
  const [preguntas, setPreguntas] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [respuestaUsuario, setRespuestaUsuario] = useState('');
  const [mensajeError, setMensajeError] = useState('');
  const [juegoFinalizado, setJuegoFinalizado] = useState(false);
  const [respuestasCorrectas, setRespuestasCorrectas] = useState(0);
  const [respuestasIncorrectas, setRespuestasIncorrectas] = useState(0);
  const [preguntasIncorrectas, setPreguntasIncorrectas] = useState([]);
  
  const db = getDatabase();

  useEffect(() => {
    // Realizar la solicitud HTTP para obtener todas las preguntas disponibles
    fetch('http://143.198.98.190:8000/preguntas/')
      .then((response) => response.json())
      .then((data) => {
        // Seleccionar aleatoriamente 10 preguntas sin repetición
        const randomQuestions = selectRandomQuestions(data, 10);
        setPreguntas(randomQuestions);
      })
      .catch((error) => {
        console.error('Error al obtener las preguntas:', error);
        setMensajeError('No se pudieron cargar las preguntas. Inténtalo de nuevo más tarde.');
      });
  }, []);

  const selectRandomQuestions = (questions, count) => {
    if (questions.length <= count) {
      // Si hay menos o igual cantidad de preguntas disponibles que las requeridas, devolver todas
      return questions;
    } else {
      // Usar algoritmo para seleccionar aleatoriamente sin repetición
      const shuffledQuestions = questions.slice();
      for (let i = shuffledQuestions.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledQuestions[i], shuffledQuestions[j]] = [shuffledQuestions[j], shuffledQuestions[i]];
      }
      return shuffledQuestions.slice(0, count);
    }
  };

  const handleHintClick = () => {
    setShowHint(true);
  };

  const handleRespuestaChange = (e) => {
    setRespuestaUsuario(e.target.value);
  };

  const handleVerificarRespuesta = async () => {
    if (currentQuestionIndex < preguntas.length) {
      const question = preguntas[currentQuestionIndex];

      if (respuestaUsuario === question.respuesta) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setRespuestaUsuario('');
        setShowHint(false);
        setMensajeError('');
        setRespuestasCorrectas(respuestasCorrectas + 1);

        const usuarioId = user.uid;
        if (!usuarioId) {
          console.error('ID de usuario no válido');
          return;
        }

        const preguntasBuenasRef = ref(db, `usuarios/` + user.uid + `/preguntas_buenas`);
        push(preguntasBuenasRef, question.id);
      } else {
        setPreguntasIncorrectas([...preguntasIncorrectas, question]);
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setRespuestaUsuario('');
        setShowHint(false);
        setMensajeError('');
        setRespuestasIncorrectas(respuestasIncorrectas + 1);

        const usuarioId = user.uid;
        if (!usuarioId) {
          console.error('ID de usuario no válido');
          return;
        }

        const preguntasMalasRef = ref(db, `usuarios/${usuarioId}/preguntas_malas`);
        push(preguntasMalasRef, question.id);
      }

      if (currentQuestionIndex === preguntas.length - 1) {
        setJuegoFinalizado(true);
      }
    }
  };

  const handleSeleccionarAlternativa = (alternativa) => {
    if (currentQuestionIndex < preguntas.length) {
      const question = preguntas[currentQuestionIndex];
      if (alternativa === question.respuesta) {
        setCurrentQuestionIndex(currentQuestionIndex + 1);
        setRespuestaUsuario('');
        setShowHint(false);
        setMensajeError('');
        setRespuestasCorrectas(respuestasCorrectas + 1);

        if (currentQuestionIndex === preguntas.length - 1) {
          setJuegoFinalizado(true);
        }
      } else {
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
};

export default PreguntasPage;
