import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { getDatabase, ref, get } from 'firebase/database';

function ViewQuestion() {
  const { id } = useParams();
  const [pregunta, setPregunta] = useState(null);

  useEffect(() => {
    const db = getDatabase();
    const preguntaRef = ref(db, `preguntas/${id}`);

    get(preguntaRef)
      .then((snapshot) => {
        if (snapshot.exists()) {
          const preguntaData = snapshot.val();
          setPregunta(preguntaData);
        } else {
          console.log('No se encontró la pregunta.');
        }
      })
      .catch((error) => {
        console.error('Error al obtener la pregunta:', error);
        
      });
  }, [id]);

  return (
    <div>
      <h1>Detalles de la Pregunta</h1>
      {pregunta ? (
        <div><strong>ID:</strong> {pregunta.id}
        <br />
        <strong>tema:</strong> {pregunta.tema}
        <br />
        <strong>Nivel de dificultad:</strong> {pregunta.nivel_dificultad}
        <br />
          <strong>Enunciado:</strong> {pregunta.enunciado}
          <br />
          <strong>Alternativa 1:</strong> {pregunta.alternativa1}
          <br />
          <strong>Alternativa 2:</strong> {pregunta.alternativa2}
          <br />
          <strong>Alternativa 3:</strong> {pregunta.alternativa3}
          <br />
          <strong>Alternativa 4:</strong> {pregunta.alternativa4}
          <br />
          <strong>Respuesta:</strong> {pregunta.respuesta}
          <br />
          <strong>Hint:</strong> {pregunta.hint}
          {/* Puedes mostrar más detalles aquí si es necesario */}
        </div>
      ) : (
        <p>Cargando pregunta...</p>
      )}
    </div>
  );
}

export default ViewQuestion;
