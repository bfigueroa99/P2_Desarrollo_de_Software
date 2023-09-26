// ViewQuestion.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ViewQuestion({ match }) {
  const [question, setQuestion] = useState(null);

  useEffect(() => {
    // Obtener la pregunta con el ID correspondiente desde la API de Django
    axios.get(`http://143.198.98.190:8000/preguntas/${match.params.id}/`)
      .then((response) => {
        setQuestion(response.data);
      })
      .catch((error) => {
        console.error('Error al obtener la pregunta:', error);
      });
  }, [match.params.id]);

  if (!question) {
    return <div>Cargando...</div>;
  }

  return (
    <div>
      <h1>Detalles de la Pregunta</h1>
      <p>ID: {question.id}</p>
      <p>Tema: {question.tema}</p>
      <p>Tipo: {question.tipo}</p>
      <p>Nivel de Dificultad: {question.nivel_dificultad}</p>
      <p>Enunciado: {question.enunciado}</p>
      {/* Mostrar otros campos de pregunta aquí */}
      <p>Respuesta: {question.respuesta}</p>
      <p>Pista: {question.hint}</p>
      {/* Puedes mostrar la imagen SVG aquí si es necesario */}
    </div>
  );
}

export default ViewQuestion;
