import React from 'react';
import { BrowserRouter as Router,Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar//NavBar'; 
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
        <NavBar />
        {/* Define las rutas de tu aplicación */}
        <Routes>
          <Route path="/" exact component={HomePage} />
          <Route path="/account" component={AccountPage} />
          <Route path="/about" component={AboutUsPage} />
          <Route path="/help" component={HelpPage} />
          <Route path="/courses" exact component={CoursesPage} />
          <Route path="/login" component={LoginPage} />
          <Route path="/signup" component={SignPage} />
          <Route path="/courses/:courseId/start" component={StartPage} />
          <Route path="/courses/:courseId/start/questions" component={PreguntasPage} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

