import React from 'react';
import './AccountPage.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { useAuth } from '../../auth/AuthProvider'; // Importa tu contexto de autenticación aquí

function AccountPage() {
  const { user } = useAuth(); // Obtén el usuario actual del contexto de autenticación

  // Simulación de datos de progreso del curso
  const courseProgress = [
    { unit: 'Unidad 1', progress: 80 },
    { unit: 'Unidad 2', progress: 60 },
    { unit: 'Unidad 3', progress: 90 },
    { unit: 'Unidad 4', progress: 75 },
    { unit: 'Unidad 5', progress: 50 },
  ];

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
            </>
          ) : (
            <>
              <h2 className="user-name">Usuario no autenticado</h2>
              <p className="user-email">N/A</p>
            </>
          )}
        </div>
      </div>

      <h2 className="progress-title">Progreso del Curso</h2>
      <div className="course-progress">
        {courseProgress.map((item, index) => (
          <div className="progress-item" key={index}>
            <p className="unit-name">{item.unit}</p>
            <div className="progress-bar">
              <div className="progress-fill" style={{ width: `${item.progress}%` }}></div>
            </div>
            <p className="progress-value">{item.progress}%</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AccountPage;
