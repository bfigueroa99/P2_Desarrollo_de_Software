import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function ViewQuestion() {
  const { id } = useParams();
  const [pregunta, setPregunta] = useState({
    id: null,
    imagen_svg: null,
    tema: '',
    tipo: '',
    nivel_dificultad: '',
    enunciado: '',
    alternativa1: null,
    alternativa2: null,
    alternativa3: null,
    alternativa4: null,
    respuesta: '',
    hint: '',
  });

  useEffect(() => {
    // Realiza una solicitud para obtener los detalles de la pregunta a ver
    axios.get(`http://143.198.98.190:8000/preguntas/${id}/`)
      .then((response) => {
        setPregunta(response.data);
      })
      .catch((error) => {
        console.error('Error al obtener la pregunta:', error);
      });
  }, [id]);

  return (
    <div>
      <h1>Detalles de la Pregunta</h1>
      <div>
        <strong>Enunciado:</strong> {pregunta.enunciado}
      </div>
      <div>
        <strong>Alternativa 1:</strong> {pregunta.alternativa1}
      </div>
      <div>
        <strong>Alternativa 2:</strong> {pregunta.alternativa2}
      </div>
      <div>
        <strong>Alternativa 3:</strong> {pregunta.alternativa3}
      </div>
      <div>
        <strong>Alternativa 4:</strong> {pregunta.alternativa4}
      </div>
      <div>
        <strong>Respuesta:</strong> {pregunta.respuesta}
      </div>
      <div>
        <strong>Hint:</strong> {pregunta.hint}
      </div>
      {/* Puedes mostrar más detalles aquí si es necesario */}
    </div>
  );
}

export default ViewQuestion;
