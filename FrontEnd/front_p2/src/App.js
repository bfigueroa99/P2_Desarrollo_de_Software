import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Asegúrate de importar Routes

import HomePage from './components/HomePage/HomePage';
import AccountPage from './components/AccountPage/AccountPage';
import AboutUsPage from './components/AboutUsPage/AboutUsPage';
import HelpPage from './components/HelpPage/HelpPage';
import CoursesPage from './components/CoursesPage/CoursesPage';
import LoginPage from './components/LoginPage/LoginPage';
import SignPage from './components/SignPage/SignPage';
import StartPage from './components/StartPage/StartPage';
import PreguntasPage from './components/PreguntasPage/PreguntasPage';

function App() {
  return (
    <Router>
      <div>
        {/* Agrega tu barra de navegación aquí */}
        {/* Puedes utilizar una barra de navegación común en todos los componentes */}
        
        {/* Define las rutas de tu aplicación dentro de un elemento Routes */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/account" element={<AccountPage />} />
          <Route path="/about" element={<AboutUsPage />} />
          <Route path="/help" element={<HelpPage />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignPage />} />
          <Route path="/courses/:courseId/start" element={<StartPage />} />
          <Route path="/courses/:courseId/start/questions" element={<PreguntasPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;


