import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom'; // Importa 'useParams' para obtener el ID de la pregunta desde la URL

function EditQuestion() {
  const navigate = useNavigate();
  const { id } = useParams(); // Obtiene el ID de la pregunta desde la URL

  // Estado para almacenar los detalles de la pregunta que se está editando
  const [questionDetails, setQuestionDetails] = useState({
    id: '', // Puedes inicializar otros campos aquí
    enunciado: '',
    nivel_dificultad: '',
    tipo: '',
    // Otros campos de pregunta
  });

  // Función para manejar cambios en los campos del formulario
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setQuestionDetails({
      ...questionDetails,
      [name]: value,
    });
  };

  // Función para cargar los detalles de la pregunta desde la API cuando el componente se monta
  useEffect(() => {
    // Realiza una solicitud GET para obtener los detalles de la pregunta con el ID proporcionado
    axios.get(`http://143.198.98.190:8000/preguntas/${id}/editar/`)
      .then((response) => {
        // Actualiza el estado 'questionDetails' con los detalles de la pregunta
        setQuestionDetails(response.data);
      })
      .catch((error) => {
        console.error('Error al cargar los detalles de la pregunta:', error);
      });
  }, [id]); // Ejecuta esta solicitud cuando 'id' cambia

  // Función para enviar la solicitud de edición al servidor (usar axios.put)
  const editarPregunta = () => {
    // Realiza la solicitud PUT a la API de Django para editar la pregunta con los datos en 'questionDetails'
    axios.put(`http://143.198.98.190:8000/preguntas/${id}/editar/`, questionDetails)
      .then((response) => {
        console.log('Pregunta editada con éxito:', response.data);
        // Redirige al usuario a la vista de detalles de la pregunta después de la edición
        navigate(`/preguntas/${id}/view`);
      })
      .catch((error) => {
        console.error('Error al editar la pregunta:', error);
      });
  };

  return (
    <div>
      <h1>Editar Pregunta</h1>
      <form>
        {/* Campos de edición de pregunta */}
        <input
          type="text"
          name="enunciado"
          value={questionDetails.enunciado}
          onChange={handleInputChange}
          placeholder="Enunciado"
        />
        {/* Otros campos de edición */}
        <button type="button" onClick={editarPregunta}>Guardar Cambios</button>
      </form>
    </div>
  );
}

export default EditQuestion;
