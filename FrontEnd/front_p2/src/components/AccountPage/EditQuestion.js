import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import { getDatabase, ref, set, get } from 'firebase/database'; 

function EditQuestion() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [pregunta, setPregunta] = useState({
    enunciado: '',
    alternativa1: '',
    alternativa2: '',
    alternativa3: '',
    alternativa4: '',
    respuesta: '',
    hint: '',
    tema: '',               // Agrega campo "tema"
    id: '',                 // Agrega campo "id"
    nivel_dificultad: '',   // Agrega campo "nivel_dificultad"
  });

  const [editedPregunta, setEditedPregunta] = useState({
    enunciado: '',
    alternativa1: '',
    alternativa2: '',
    alternativa3: '',
    alternativa4: '',
    respuesta: '',
    hint: '',
    tema: '',               // Agrega campo "tema"
    id: '',                 // Agrega campo "id"
    nivel_dificultad: '',   // Agrega campo "nivel_dificultad"
  });

  useEffect(() => {
    const db = getDatabase();
    const preguntaRef = ref(db, `preguntas/${id}`);

    // Obtiene los detalles de la pregunta a editar
    get(preguntaRef)
      .then((snapshot) => {
        if (snapshot.exists()) {
          const preguntaData = snapshot.val();
          setPregunta(preguntaData);
          setEditedPregunta(preguntaData);
        } else {
          console.log('No se encontró la pregunta.');
        }
      })
      .catch((error) => {
        console.error('Error al obtener la pregunta:', error);
      });
  }, [id]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setEditedPregunta({
      ...editedPregunta,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const db = getDatabase();
    const preguntaRef = ref(db, `preguntas/${id}`);

    // Actualiza la pregunta en Firebase Realtime Database
    set(preguntaRef, editedPregunta)
      .then(() => {
        console.log('Pregunta actualizada con éxito.');

        // Redirige al usuario a la vista de la pregunta actualizada
        navigate(`/view/${id}`);
      })
      .catch((error) => {
        console.error('Error al actualizar la pregunta:', error);
      });
  };

  return (
    <div>
      <h1>Editar Pregunta</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="enunciado">Enunciado</label>
          <input
            type="text"
            id="enunciado"
            name="enunciado"
            value={editedPregunta.enunciado}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa1">Alternativa 1</label>
          <input
            type="text"
            id="alternativa1"
            name="alternativa1"
            value={editedPregunta.alternativa1}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa2">Alternativa 2</label>
          <input
            type="text"
            id="alternativa2"
            name="alternativa2"
            value={editedPregunta.alternativa2}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa3">Alternativa 3</label>
          <input
            type="text"
            id="alternativa3"
            name="alternativa3"
            value={editedPregunta.alternativa3}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa4">Alternativa 4</label>
          <input
            type="text"
            id="alternativa4"
            name="alternativa4"
            value={editedPregunta.alternativa4}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="respuesta">Respuesta</label>
          <input
            type="text"
            id="respuesta"
            name="respuesta"
            value={editedPregunta.respuesta}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="hint">Hint</label>
          <input
            type="text"
            id="hint"
            name="hint"
            value={editedPregunta.hint}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="tema">Tema</label>
          <input
            type="text"
            id="tema"
            name="tema"
            value={editedPregunta.tema}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="id">ID</label>
          <input
            type="text"
            id="id"
            name="id"
            value={editedPregunta.id}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="nivel_dificultad">Nivel de Dificultad</label>
          <input
            type="text"
            id="nivel_dificultad"
            name="nivel_dificultad"
            value={editedPregunta.nivel_dificultad}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Guardar Cambios</button>
      </form>
    </div>
  );
}

export default EditQuestion;
