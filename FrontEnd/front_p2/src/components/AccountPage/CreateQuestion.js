// CreateQuestion.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
function CreateQuestion() {
  const navigate =useNavigate()
  // Estado para almacenar los detalles de la nueva pregunta
  const [newQuestion, setNewQuestion] = useState({
    // Inicializa los campos de la pregunta (puedes establecer valores iniciales aquí)
    enunciado: '',
    nivel_dificultad: '',
    tipo: '',
    // Otros campos de pregunta
  });

  // Función para manejar cambios en los campos del formulario
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setNewQuestion({
      ...newQuestion,
      [name]: value,
    });
  };

  // Función para enviar la solicitud de creación al servidor (usar axios.post)
  const crearPregunta = () => {
    // Realiza la solicitud POST a la API de Django para crear una nueva pregunta con los datos en 'newQuestion'
    axios.post('http://143.198.98.190:8000/preguntas/', newQuestion)
      .then((response) => {
        console.log('Pregunta creada con éxito:', response.data);
        // Puedes redirigir al usuario a la página de lista de preguntas después de la creación
        navigate.push('/preguntas');
      })
      .catch((error) => {
        console.error('Error al crear la pregunta:', error);
      });
  };

  return (
    <div>
      <h1>Crear Nueva Pregunta</h1>
      <form>
        {/* Campos de creación de pregunta */}
        <input
          type="text"
          name="enunciado"
          value={newQuestion.enunciado}
          onChange={handleInputChange}
          placeholder="Enunciado"
        />
        {/* Otros campos de creación */}
        <button type="button" onClick={crearPregunta}>Crear Pregunta</button>
      </form>
    </div>
  );
}

export default CreateQuestion;
