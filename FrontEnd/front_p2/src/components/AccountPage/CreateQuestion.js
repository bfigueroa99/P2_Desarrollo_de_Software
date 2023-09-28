import React, { useState } from 'react';
import axios from 'axios';

function CreateQuestion() {
  const [newPregunta, setNewPregunta] = useState({
    enunciado: '',
    alternativa1: '',
    alternativa2: '',
    alternativa3: '',
    alternativa4: '',
    respuesta: '',
    hint: '',
    tipo: 'alternativa', // Valor predeterminado para el campo tipo
    nivel: 'baja', // Valor predeterminado para el campo nivel
    // nivel_dificultad: 'baja', // Valor predeterminado para el campo nivel_dificultad
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setNewPregunta({
      ...newPregunta,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Realiza una solicitud HTTP POST para crear una nueva pregunta
    axios.post('http://143.198.98.190:8000/preguntas/crear/', newPregunta)
      .then((response) => {
        // Maneja la respuesta, por ejemplo, muestra un mensaje de éxito
        console.log('Pregunta creada con éxito.');
      })
      .catch((error) => {
        console.error('Error al crear la pregunta:', error.response.data);
      });
  };

  return (
    <div>
      <h1>Crear Pregunta</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="enunciado">Enunciado</label>
          <input
            type="text"
            id="enunciado"
            name="enunciado"
            value={newPregunta.enunciado}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa1">Alternativa 1</label>
          <input
            type="text"
            id="alternativa1"
            name="alternativa1"
            value={newPregunta.alternativa1}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa2">Alternativa 2</label>
          <input
            type="text"
            id="alternativa2"
            name="alternativa2"
            value={newPregunta.alternativa2}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa3">Alternativa 3</label>
          <input
            type="text"
            id="alternativa3"
            name="alternativa3"
            value={newPregunta.alternativa3}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="alternativa4">Alternativa 4</label>
          <input
            type="text"
            id="alternativa4"
            name="alternativa4"
            value={newPregunta.alternativa4}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="respuesta">Respuesta</label>
          <input
            type="text"
            id="respuesta"
            name="respuesta"
            value={newPregunta.respuesta}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="hint">Hint</label>
          <input
            type="text"
            id="hint"
            name="hint"
            value={newPregunta.hint}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="nivel">Nivel</label>
          <select
            id="nivel"
            name="nivel"
            value={newPregunta.nivel}
            onChange={handleInputChange}
          >
            <option value="alta">Alta</option>
            <option value="media">Media</option>
            <option value="baja">Baja</option>
          </select>
        </div>
        <button type="submit">Crear Pregunta</button>
      </form>
    </div>
  );
}

export default CreateQuestion;
