import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
function EditQuestion() {
  const { id } = useParams();
  const navigate = useNavigate();
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

  const [editedPregunta, setEditedPregunta] = useState({
    enunciado: '',
    alternativa1: '',
    alternativa2: '',
    alternativa3: '',
    alternativa4: '',
    respuesta: '',
    hint: '',
  });

  useEffect(() => {
    // Realiza una solicitud para obtener los detalles de la pregunta a editar
    axios.get(`http://143.198.98.190:8000/preguntas/${id}/`)
      .then((response) => {
        setPregunta(response.data);
        setEditedPregunta({
          enunciado: response.data.enunciado,
          alternativa1: response.data.alternativa1 || '',
          alternativa2: response.data.alternativa2 || '',
          alternativa3: response.data.alternativa3 || '',
          alternativa4: response.data.alternativa4 || '',
          respuesta: response.data.respuesta,
          hint: response.data.hint || '',
          tipo: response.data.tipo, // Agrega el campo tipo
          nivel_dificultad: response.data.nivel_dificultad, // Agrega el campo nivel_dificultad
        });
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

    editedPregunta.tipo = pregunta.tipo;
    editedPregunta.nivel_dificultad = pregunta.nivel_dificultad;

    // Realiza una solicitud HTTP PUT para actualizar la pregunta
    axios.put(`http://143.198.98.190:8000/preguntas/${id}/editar/`, editedPregunta)
      .then((response) => {
        // Maneja la respuesta, por ejemplo, muestra un mensaje de éxito
        console.log('Pregunta actualizada con éxito.');
        navigate('/account');
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
        <button type="submit">Guardar Cambios</button>
      </form>
    </div>
  );
}

export default EditQuestion;





// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import { useParams } from 'react-router-dom';

// function EditQuestion() {
//   const { id } = useParams();
//   const [pregunta, setPregunta] = useState({
//     id: null,
//     imagen_svg: null,
//     tema: '',
//     tipo: '',
//     nivel_dificultad: '',
//     enunciado: '',
//     alternativa1: null,
//     alternativa2: null,
//     alternativa3: null,
//     alternativa4: null,
//     respuesta: '',
//     hint: '',
//   });

//   const [editedPregunta, setEditedPregunta] = useState({
//     enunciado: '',
//     alternativa1: '',
//     alternativa2: '',
//     alternativa3: '',
//     alternativa4: '',
//     respuesta: '',
//     hint: '',
//   });

//   useEffect(() => {
//     // Realiza una solicitud para obtener los detalles de la pregunta a editar
//     axios.get(`http://143.198.98.190:8000/preguntas/${id}/`)
//       .then((response) => {
//         setPregunta(response.data);
//         setEditedPregunta({
//           enunciado: response.data.enunciado,
//           alternativa1: response.data.alternativa1 || '',
//           alternativa2: response.data.alternativa2 || '',
//           alternativa3: response.data.alternativa3 || '',
//           alternativa4: response.data.alternativa4 || '',
//           respuesta: response.data.respuesta,
//           hint: response.data.hint || '',
//         });
//       })
//       .catch((error) => {
//         console.error('Error al obtener la pregunta:', error);
//       });
//   }, [id]);

//   const handleInputChange = (event) => {
//     const { name, value } = event.target;
//     setEditedPregunta({
//       ...editedPregunta,
//       [name]: value,
//     });
//   };

//   const handleSubmit = (event) => {
//     event.preventDefault();

//     // Realiza una solicitud HTTP PUT para actualizar la pregunta
//     axios.put(`http://143.198.98.190:8000/preguntas/${id}/editar`, editedPregunta)
//       .then((response) => {
//         // Maneja la respuesta, por ejemplo, muestra un mensaje de éxito
//         console.log('Pregunta actualizada con éxito.');
//       })
//       .catch((error) => {
//         console.error('Error al actualizar la pregunta:', error);
//       });
//   };

//   return (
//     <div>
//       <h1>Editar Pregunta</h1>
//       <form onSubmit={handleSubmit}>
//         <div>
//           <label htmlFor="enunciado">Enunciado</label>
//           <input
//             type="text"
//             id="enunciado"
//             name="enunciado"
//             value={editedPregunta.enunciado}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div>
//           <label htmlFor="alternativa1">Alternativa 1</label>
//           <input
//             type="text"
//             id="alternativa1"
//             name="alternativa1"
//             value={editedPregunta.alternativa1}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div>
//           <label htmlFor="alternativa2">Alternativa 2</label>
//           <input
//             type="text"
//             id="alternativa2"
//             name="alternativa2"
//             value={editedPregunta.alternativa2}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div>
//           <label htmlFor="alternativa3">Alternativa 3</label>
//           <input
//             type="text"
//             id="alternativa3"
//             name="alternativa3"
//             value={editedPregunta.alternativa3}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div>
//           <label htmlFor="alternativa4">Alternativa 4</label>
//           <input
//             type="text"
//             id="alternativa4"
//             name="alternativa4"
//             value={editedPregunta.alternativa4}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div>
//           <label htmlFor="respuesta">Respuesta</label>
//           <input
//             type="text"
//             id="respuesta"
//             name="respuesta"
//             value={editedPregunta.respuesta}
//             onChange={handleInputChange}
//           />
//         </div>
//         <div>
//           <label htmlFor="hint">Hint</label>
//           <input
//             type="text"
//             id="hint"
//             name="hint"
//             value={editedPregunta.hint}
//             onChange={handleInputChange}
//           />
//         </div>
//         <button type="submit">Guardar Cambios</button>
//       </form>
//     </div>
//   );
// }

// export default EditQuestion;
