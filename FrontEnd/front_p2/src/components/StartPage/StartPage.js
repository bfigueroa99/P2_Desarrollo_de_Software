import React from 'react';
import { Link } from 'react-router-dom';
import './StartPage.css';

function StartPage() {
  return (
    
    <div className="start-page">
      <h1>¡Comienza el Curso!</h1>
      <Link to="/questions">
        <div className="start-card">
          <h2>Comenzar</h2>
          <p>Haz clic para comenzar las preguntas.</p>
        </div>
      </Link>
      
    </div>
  );
}

export default StartPage;
