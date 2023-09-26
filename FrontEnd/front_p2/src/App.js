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
import EditQuestion from './components/AccountPage/EditQuestion';
import CreateQuestion from './components/AccountPage/CreateQuestion';
import ViewQuestion from './components/AccountPage/ViewQuestion';
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
        <Route path="/:id/edit/" component={EditQuestion} />
        <Route path="/create" component={CreateQuestion} />
        <Route path="/:id/view" component={ViewQuestion} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
