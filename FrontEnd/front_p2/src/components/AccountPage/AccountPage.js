import React, { useState, useEffect } from 'react';
import './AccountPage.css';
import { useAuth } from '../../auth/AuthProvider';
import { getDatabase, ref, get, DataSnapshot, remove } from 'firebase/database'; // Importa las funciones necesarias para Firebase Realtime Database

import { useNavigate } from 'react-router-dom';

function AccountPage() {
  const { user } = useAuth();
  const [userRole, setUserRole] = useState(null);
  const [alumnos, setAlumnos] = useState([]);
  const [preguntas, setPreguntas] = useState([]);
  const [userProgress, setUserProgress] = useState({ nivel: 0, puntaje: 0 });
  const navigate = useNavigate();

  useEffect(() => {
    const db = getDatabase();
    if (user) {
      const userRef = ref(db, 'usuarios/' + user.uid);

      get(userRef)
        .then((snapshot) => {
          if (snapshot.exists()) {
            setUserRole(snapshot.val().rol);
            setUserProgress(snapshot.val());
          } else {
            console.log('El usuario no tiene datos de rol en la base de datos.');
          }
        })
        .catch((error) => {
          console.error('Error al obtener datos de rol:', error);
        });
    }
  }, [user]);

  useEffect(() => {
    if (userRole === 'profesor') {
      const db = getDatabase();
      const alumnosRef = ref(db, 'usuarios');
      get(alumnosRef)
        .then((snapshot) => {
          if (snapshot.exists()) {
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

      const preguntasRef = ref(db, 'preguntas');
      get(preguntasRef)
        .then((snapshot) => {
          if (snapshot.exists()) {
            const preguntasList = [];
            snapshot.forEach((childSnapshot) => {
              const preguntaData = childSnapshot.val();
              preguntasList.push(preguntaData);
            });
            setPreguntas(preguntasList);
          } else {
            console.log('No hay datos de preguntas en la base de datos.');
          }
        })
        .catch((error) => {
          console.error('Error al obtener datos de preguntas:', error);
        });
    }
  }, [userRole]);

  const eliminarPregunta = (preguntaId) => {
    const db = getDatabase();
    const preguntaRef = ref(db, `preguntas/${preguntaId}`);
  
    // Utiliza el método remove en la referencia para eliminar el nodo
    remove(preguntaRef)
      .then(() => {
        setPreguntas((prevPreguntas) => prevPreguntas.filter((pregunta) => pregunta.id !== preguntaId));
        console.log('Pregunta eliminada con éxito.');
      })
      .catch((error) => {
        console.error('Error al eliminar la pregunta:', error);
      });
  };

  const editarPregunta = (id) => {
    navigate(`/edit/${id}`);
  };

  const crearPregunta = () => {
    navigate('/create');
  };

  const verPregunta = (id) => {
    // Redirige al usuario a la vista de pregunta específica
    navigate(`/view/${id}`); // Asegúrate de que la URL sea correcta según tu estructura de datos en Firebase Realtime Database
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
