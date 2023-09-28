import React, { useState, useEffect } from 'react';
import './PreguntasPage.css';
import axios from 'axios';

function PreguntasPage() {
  const [showHint, setShowHint] = useState(false);
  const [preguntaActual, setPreguntaActual] = useState(null);
  const [respuestaUsuario, setRespuestaUsuario] = useState('');
  const [mensajeError, setMensajeError] = useState('');
  const [juegoFinalizado, setJuegoFinalizado] = useState(false);
  const [respuestasCorrectas, setRespuestasCorrectas] = useState(0);
  const [respuestasIncorrectas, setRespuestasIncorrectas] = useState(0);
  const [preguntasIncorrectas, setPreguntasIncorrectas] = useState([]);
  const [segundaOportunidad, setSegundaOportunidad] = useState(false);
  // Método DELETE
  const handleEliminarTodasLasRespuestas = () => {
    axios.delete('http://127.0.0.1:8000/eliminar-todas-las-respuestas/')
      .then((response) => {
        console.log('listeilor')
        // Manejar la respuesta del servidor si es necesario
      })
      .catch((error) => {
        console.error('Error al eliminar todas las respuestas:', error);
      });
  };
  useEffect(() => {
    handleEliminarTodasLasRespuestas();
    // Paso 1: Obtener la primera pregunta
    axios.post('http://143.198.98.190:8000/seleccionar_primera_pregunta/', {
      nivel_estudiante: 1,
      tema: "Diagramas de PVT"
    })
    .then((response) => {
      setPreguntaActual(response.data);
    })
    .catch((error) => {
      console.error('Error al obtener la primera pregunta:', error);
    });
  }, []);

  const handleHintClick = () => {
    setShowHint(true);
  };

  const handleRespuestaChange = (e) => {
    setRespuestaUsuario(e.target.value);
  };

  const handleVerificarRespuesta = () => {
    if (preguntaActual) {
      const question = preguntaActual;

      // Paso 2: Registrar la respuesta del estudiante
      axios.post('http://143.198.98.190:8000/api/registrar_respuesta/', {
        pregunta_relacionada: question.id,
        respuesta_estudiante: respuestaUsuario,
        uso_hint: false,
        respondida_correctamente: false, // Inicialmente asumimos que la respuesta es incorrecta
        tipo_pregunta: question.tipo,
        tema: "Diagramas de PVT"
      })
      .then((response) => {
        // Actualizar el estado según la respuesta del servidor (respondida_correctamente)
        if (response.data.respondida_correctamente) {
          
          setRespuestasCorrectas(respuestasCorrectas + 1);
        } else {
          
          setRespuestasIncorrectas(respuestasIncorrectas + 1);
          setPreguntasIncorrectas([...preguntasIncorrectas, question]);
        }

        // Paso 3: Obtener el registro de respuestas
        axios.get('http://143.198.98.190:8000/respuestas')
        .then((response) => {
          const respuestasRegistradas = response.data;

          // Paso 4: Obtener la siguiente pregunta
          axios.post('http://143.198.98.190:8000/siguiente_pregunta/', {
            preguntas_respondidas: respuestasRegistradas,
            nivel_alumno: 5
          })
          .then((response) => {
            const siguientePregunta = response.data;
            
            if (siguientePregunta.error === "No hay más preguntas disponibles") {
              setJuegoFinalizado(true);
            } else {
              setPreguntaActual(siguientePregunta);
            }
          })
          .catch((error) => {
            console.error('Error al obtener la siguiente pregunta:', error);
          });
        })
        .catch((error) => {
          console.error('Error al obtener el registro de respuestas:', error);
        });
      })
      .catch((error) => {
        console.error('Error al registrar la respuesta:', error);
      });
    }
  };

  const handleSeleccionarAlternativa = (alternativa) => {
    if (preguntaActual) {
      const question = preguntaActual;
  
      // Mapear el número de alternativa a la respuesta correspondiente
      let respuestaCorrecta = '';
      switch (alternativa) {
        case '1':
          respuestaCorrecta = question.alternativa1;
          break;
        case '2':
          
          respuestaCorrecta = question.alternativa2;
          break;
        case '3':
          
          respuestaCorrecta = question.alternativa3;
          break;
        case '4':
          
          respuestaCorrecta = question.alternativa4;
          break;
        default:
          break;
      }
  
      if (respuestaCorrecta === question.respuesta) {
        // Respuesta correcta: actualizar el estado y el contador de respuestas correctas
        setRespuestaUsuario('');
        setRespuestasCorrectas(respuestasCorrectas + 1);
  
        // Comprobar si se han respondido todas las preguntas
        if (segundaOportunidad || preguntasIncorrectas.length === 0) {
          setJuegoFinalizado(true);
        } else {
          setSegundaOportunidad(true);
          setPreguntaActual(preguntasIncorrectas[0]); // Obtener la primera pregunta incorrecta
          setPreguntasIncorrectas(preguntasIncorrectas.slice(1)); // Eliminar la primera pregunta incorrecta
        }
      } else {
        // Respuesta incorrecta en la primera oportunidad: agregar la pregunta a la lista de preguntas incorrectas
        setPreguntasIncorrectas([...preguntasIncorrectas, question]);
        setRespuestasIncorrectas(respuestasIncorrectas + 1);
      }
    }
  };
  
  

  return (
    <div className="questions-page">
      <h1>Preguntas y Respuestas</h1>

      {juegoFinalizado ? (
        // Mostrar estadísticas y mensaje de juego finalizado
        <div>
          <p>Juego finalizado, has respondido todo.</p>
          <p>Respuestas correctas: {respuestasCorrectas}</p>
          <p>Respuestas incorrectas: {respuestasIncorrectas}</p>
        </div>
      ) : preguntaActual ? (
        // Mostrar la pregunta actual
        <div className="question-card">
          <h2>Pregunta {preguntaActual.id}</h2>

          <p>{preguntaActual.enunciado}</p>
          {preguntaActual.tipo === 'alternativas' ? (
            // Renderizar opciones de respuesta para preguntas de alternativas
            <div className="answer-options">
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('1')}>1. {preguntaActual.alternativa1}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('2')}>2. {preguntaActual.alternativa2}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('3')}>3. {preguntaActual.alternativa3}</button>
              <button className="answer-button" onClick={() => handleSeleccionarAlternativa('4')}>4. {preguntaActual.alternativa4}</button>
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
            {showHint && <span className="hint-popup">{preguntaActual.hint}</span>}
          </button>
          {mensajeError && <p className="error-message">{mensajeError}</p>}
        </div>
      ) : (
        // Mostrar un mensaje de carga mientras se obtienen las preguntas
        <p>Cargando preguntas...</p>
      )}
    </div>
  );
}

export default PreguntasPage;
