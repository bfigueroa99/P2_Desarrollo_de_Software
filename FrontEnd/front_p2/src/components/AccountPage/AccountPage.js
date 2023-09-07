import React from 'react';
import './AccountPage.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

function AccountPage() {
  // Simulación de datos de usuario y progreso del curso
  const user = {
    name: 'Nombre del Usuario',
    email: 'usuario@example.com',
    profilePicture: <FontAwesomeIcon icon=" fa-regular fa-user"size="4x"/>,
  };

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
        <img src={user.profilePicture} alt="Foto de perfil" className="profile-picture" />
        <div className="user-info">
          <h2 className="user-name">{user.name}</h2>
          <p className="user-email">{user.email}</p>
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
