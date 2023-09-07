import React from 'react';
import { Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar/NavBar';
import HomePage from './components/HomePage/HomePage';
import AccountPage from './components/AccountPage/AccountPage';
import AboutUsPage from './components/AboutUsPage/AboutUsPage';
import HelpPage from './components/HelpPage/HelpPage';
import CoursesPage from './components/CoursesPage/CoursesPage';
import LoginPage from './components/LoginPage/LoginPage';
import SignPage from './components/SignPage/SignPage';
import StartPage from './components/StartPage/StartPage';
import PreguntasPage from './components/PreguntasPage/PreguntasPage';
import Footer from './components/Footer/Footer';
import PreguntasAltPage from './components/PreguntasAltPage/PreguntasAltPage';

function App() {
  return (
    <div>
      <NavBar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/account" element={<AccountPage />} />
        <Route path="/about" element={<AboutUsPage />} />
        <Route path="/help" element={<HelpPage />} />
        <Route path="/courses" element={<CoursesPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignPage />} />
        <Route path="/start" element={<StartPage />} />
        <Route path="/questions" element={<PreguntasPage />} />
        <Route path="/questionsAlt" element={<PreguntasAltPage />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
