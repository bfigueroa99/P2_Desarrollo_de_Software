import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { getDatabase, ref, push } from 'firebase/database';

function CreateQuestion() {
  const [newPregunta, setNewPregunta] = useState({
    numero: '', // Agregar campo número
    enunciado: '',
    alternativa1: '',
    alternativa2: '',
    alternativa3: '',
    alternativa4: '',
    respuesta: '',
    hint: '',
    tema: '',
    tipo: '',
    nivel_dificultad: '',
  });

  const navigate = useNavigate();

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setNewPregunta({
      ...newPregunta,
      [name]: value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const db = getDatabase();
    const preguntasRef = ref(db, 'preguntas');

    // Agregar un número de pregunta antes de crearla
    const nuevaPreguntaConNumero = {
      ...newPregunta,
      numero: obtenerProximoNumeroDePregunta(), // Llama a una función para obtener el próximo número
    };

    // Agrega la nueva pregunta a Firebase Realtime Database
    push(preguntasRef, nuevaPreguntaConNumero)
      .then((newPreguntaRef) => {
        // Obtiene el ID de la nueva pregunta creada
        const newPreguntaId = newPreguntaRef.key;
        console.log('Pregunta creada con éxito. ID:', newPreguntaId);

        // Redirige al usuario a la vista de la pregunta recién creada
        navigate(`/view/${newPreguntaId}`);
      })
      .catch((error) => {
        console.error('Error al crear la pregunta:', error);
      });
  };

  // Función para obtener el próximo número de pregunta
  const obtenerProximoNumeroDePregunta = () => {
    // Realiza una solicitud para obtener el número más alto de las preguntas existentes
    // Puedes implementar esta lógica según tus necesidades y tu estructura de datos
    // Por ejemplo, podrías consultar todas las preguntas existentes y encontrar el número más alto.
    const numeroMasAlto = 0; // Debes implementar esta lógica

    // Retorna el próximo número como una cadena (puedes ajustar el formato según tus necesidades)
    return (numeroMasAlto + 1).toString();
  };
  return (
    <div>
      <h1>Crear Pregunta</h1>
      <form onSubmit={handleSubmit}>
      <div>
          <label htmlFor="ID">id</label>
          <input
            type="nu"
            id="id"
            name="id"
            value={newPregunta.id}
            onChange={handleInputChange}
          />
        </div>
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
          <label htmlFor="tema">Tema</label>
          <input
            type="text"
            id="tema"
            name="tema"
            value={newPregunta.tema}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="nivel_dificultad">Nivel de Dificultad</label>
          <select
            id="nivel_dificultad"
            name="nivel_dificultad"
            value={newPregunta.nivel_dificultad}
            onChange={handleInputChange}
          >
            <option value="Baja">Baja</option>
            <option value="Media">Media</option>
            <option value="Alta">Alta</option>
          </select>
        </div>
        <div>
          <label htmlFor="tipo">Tipo de Pregunta</label>
          <select
            id="tipo"
            name="tipo"
            value={newPregunta.tipo}
            onChange={handleInputChange}
          >
            <option value="alternativas">Alternativas</option>
            <option value="otroTipo">Otro Tipo</option>
          </select>
        </div>
        <button type="submit">Crear Pregunta</button>
      </form>
    </div>
  );
}

export default CreateQuestion;
