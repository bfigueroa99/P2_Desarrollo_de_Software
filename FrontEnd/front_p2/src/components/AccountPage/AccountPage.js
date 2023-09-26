import React, { useState, useEffect } from 'react';
import './AccountPage.css';
import { useAuth } from '../../auth/AuthProvider'; // Importa tu contexto de autenticación aquí
import { ref, get } from 'firebase/database';
import { getDatabase } from 'firebase/database';
import axios from 'axios';
import {  useNavigate } from 'react-router-dom'; // Importa Link y usenavigate para la navegación

function AccountPage() {
  const { user } = useAuth();
  const [userRole, setUserRole] = useState(null);
  const [alumnos, setAlumnos] = useState([]);
  const [preguntas, setPreguntas] = useState([]);
  const [userProgress, setUserProgress] = useState({ nivel: 0, puntaje: 0 });
  const navigate = useNavigate(); // Objeto de historial para redirigir

  useEffect(() => {
    const db = getDatabase();
    if (user) {
      const userRef = ref(db, 'usuarios/' + user.uid);

      get(userRef)
        .then((snapshot) => {
          if (snapshot.exists()) {
            setUserRole(snapshot.val().rol);
            setUserProgress(snapshot.val()); // Actualizar el progreso del usuario
          } else {
            console.log('El usuario no tiene datos de rol en la base de datos.');
          }
        })
        .catch((error) => {
          console.error('Error al obtener datos de rol:', error);
        });

      // Consultar la lista de alumnos si el usuario es profesor
      if (userRole === 'profesor') {
        const alumnosRef = ref(db, 'usuarios');
        get(alumnosRef)
          .then((snapshot) => {
            if (snapshot.exists()) {
              // Filtrar solo a los alumnos (rol: 'alumno')
              const alumnosList = [];
              snapshot.forEach((childSnapshot) => {
                const userData = childSnapshot.val();
                if (userData.rol === 'alumno') {
                  alumnosList.push(userData);
                }
              });
              setAlumnos(alumnosList);
            } else {
              console.log('No hay datos de alumnos en la base de datos.');
            }
          })
          .catch((error) => {
            console.error('Error al obtener datos de alumnos:', error);
          });

        // Consultar las preguntas a tu API de Django
        axios.get('http://143.198.98.190:8000/preguntas/')
          .then((response) => {
            setPreguntas(response.data);
          })
          .catch((error) => {
            console.error('Error al obtener preguntas:', error);
          });
      }
    }
  }, [user, userRole]);

  // Función para eliminar una pregunta
  const eliminarPregunta = (preguntaId) => {
    // Realizar la solicitud DELETE a la API de Django para eliminar la pregunta
    axios.delete(`http://143.198.98.190:8000/preguntas/${preguntaId}/`)
      .then(() => {
        // Actualizar el estado 'preguntas' eliminando la pregunta con el ID correspondiente
        setPreguntas((prevPreguntas) => prevPreguntas.filter((pregunta) => pregunta.id !== preguntaId));
        console.log('Pregunta eliminada con éxito.');
      })
      .catch((error) => {
        console.error('Error al eliminar la pregunta:', error);
      });
  };

  // Redirigir a la vista de edición de pregunta
  const editarPregunta = (preguntaId) => {
    // Redirige a la página de edición de pregunta pasando el ID de la pregunta en la URL
    navigate(`/${preguntaId}/edit`);
  };

  // Función para crear una nueva pregunta
  const crearPregunta = () => {
    // Redirige a la página de creación de pregunta
    navigate('/create');
  };
  const verPregunta = (PreguntaId) => {
    navigate(`/${PreguntaId}/view`);
  };
  return (
    <div className="account-page">
      <h1 className="account-title">Mi Cuenta</h1>
      <div className="user-profile">
        {/* Mostrar la imagen local */}
        <img src="/images/userBlank.png" alt="Foto de perfil" className="profile-picture" />
        <div className="user-info">
          {/* Verificar si user está definido antes de acceder a sus propiedades */}
          {user ? (
            <>
              <h2 className="user-name">{user.displayName}</h2>
              <p className="user-email">{user.email}</p>
              <p className="user-nivel">Nivel: {userProgress.nivel}</p>
              <p className="user-puntaje">Puntaje: {userProgress.puntaje}</p>
            </>
          ) : (
            <>
              <h2 className="user-name">Usuario no autenticado</h2>
              <p className="user-email">N/A</p>
              <p className="user-nivel">Nivel: N/A</p>
              <p className="user-puntaje">Puntaje: N/A</p>
            </>
          )}
        </div>
      </div>

      {/* Mostrar la lista de alumnos si el usuario es profesor */}
      {userRole === 'profesor' && (
        <div>
          <h2>Lista de Alumnos</h2>
          <ul>
            {alumnos.map((alumno) => (
              <li key={alumno.uid}>
                {alumno.nombre} - Nivel: {alumno.nivel}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Mostrar las preguntas si el usuario es profesor */}
      {userRole === 'profesor' && (
        <div>
          <h2>Lista de Preguntas</h2>
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Nivel de Dificultad</th>
                <th>Tipo</th>
                <th>Enunciado</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {preguntas.map((pregunta) => (
                <tr key={pregunta.id}>
                  <td>{pregunta.id}</td>
                  <td>{pregunta.nivel_dificultad}</td>
                  <td>{pregunta.tipo}</td>
                  <td>{pregunta.enunciado}</td>
                  <td>
                    <button onClick={() => editarPregunta(pregunta.id)}>Editar</button>
                    <button onClick={() => eliminarPregunta(pregunta.id)}>Eliminar</button>
                    <button onClick={() => verPregunta(pregunta.id)}>Ver</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          <button onClick={crearPregunta}>Crear Pregunta</button>
        </div>
      )}
    </div>
  );
}

export default AccountPage;
