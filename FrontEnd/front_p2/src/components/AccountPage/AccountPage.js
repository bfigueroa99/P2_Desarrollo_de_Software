import React, { useState, useEffect } from 'react';
import './AccountPage.css';
import { useAuth } from '../../auth/AuthProvider'; // Importa tu contexto de autenticación aquí
import { ref, get, database } from 'firebase/database';
import { getDatabase } from 'firebase/database';

function AccountPage() {
  const { user } = useAuth();

  // Simulación de datos de progreso del curso
  const courseProgress = [
    { unit: 'Unidad 1', progress: 80 },
    { unit: 'Unidad 2', progress: 60 },
    { unit: 'Unidad 3', progress: 90 },
    { unit: 'Unidad 4', progress: 75 },
    { unit: 'Unidad 5', progress: 50 },
  ];

  // Obtener el nivel y puntaje del usuario desde Firebase Realtime Database
  const [userProgress, setUserProgress] = useState({ nivel: 0, puntaje: 0 });

  useEffect(() => {
    const db = getDatabase();
    if (user) {
      const userRef = ref(db, 'usuarios/' + user.uid);
      
      get(userRef).then((snapshot) => {
        if (snapshot.exists()) {
          setUserProgress(snapshot.val());
        } else {
          console.log('El usuario no tiene datos de progreso en la base de datos.');
        }
      }).catch((error) => {
        console.error('Error al obtener datos de progreso:', error);
      });
    }
  }, [user]);

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

      {/* Resto del componente */}
    </div>
  );
}

export default AccountPage;
