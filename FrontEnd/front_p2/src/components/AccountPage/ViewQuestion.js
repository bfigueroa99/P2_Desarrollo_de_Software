import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function ViewQuestion() {
  const { id } = useParams();
  const [pregunta, setPregunta] = useState(null);

  useEffect(() => {
    // Realiza una solicitud GET a la API de Django para obtener los detalles de la pregunta
    axios.get(`http://143.198.98.190:8000/preguntas/${id}`)
      .then((response) => {
        setPregunta(response.data);
      })
      .catch((error) => {
        console.error('Error al obtener los detalles de la pregunta:', error);
      });
  }, [id]);

  if (!pregunta) {
    // Muestra un mensaje de carga mientras se obtienen los datos de la pregunta
    return <div>Cargando...</div>;
  }

  return (
    <div>
      <h1>Detalles de la Pregunta</h1>
      <p>ID: {pregunta.id}</p>
      <p>Tema: {pregunta.tema}</p>
      <p>Tipo: {pregunta.tipo}</p>
      <p>Nivel de Dificultad: {pregunta.nivel_dificultad}</p>
      <p>Enunciado: {pregunta.enunciado}</p>
      <p>Alternativa1: {pregunta.alternativa1}</p>
      <p>Alternativa2: {pregunta.alternativa2}</p>
      <p>Alternativa3: {pregunta.alternativa3}</p>
      <p>Alternativa4: {pregunta.alternativa4}</p>
      <p>Respuesta: {pregunta.respuesta}</p>
      <p>Hint: {pregunta.hint}</p>
    </div>
  );
}

export default ViewQuestion;
