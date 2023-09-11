import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import './HomePage.css';

function HomePage() {
  const [showContent, setShowContent] = useState(false);

  useEffect(() => {
    // Función para manejar el scroll
    function handleScroll() {
      if (window.scrollY > 100) {
        setShowContent(true);
      } else {
        setShowContent(false);
      }
    }

    // Agrega un listener de scroll al cargar el componente
    window.addEventListener('scroll', handleScroll);

    // Remueve el listener de scroll al desmontar el componente
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  const headerVariants = {
    initial: { opacity: 0, y: -50 },
    animate: { opacity: 1, y: 0, transition: { duration: 1 } },
  };

  const textVariants = {
    initial: { opacity: 0, x: -50 },
    animate: { opacity: 1, x: 0, transition: { duration: 1, delay: 0.5 } },
  };

  const buttonVariants = {
    initial: { opacity: 0, scale: 0 },
    animate: { opacity: 1, scale: 1, transition: { duration: 0.5, delay: 1 } },
  };

  return (
    <div className={`home-page ${showContent ? 'show-content' : ''}`}>
      {/* Encabezado con imagen de fondo */}
      <div className="home-header" style={{ backgroundImage: `url('/background-image.jpg')` }}>
        <motion.div
          initial="initial"
          animate="animate"
          variants={headerVariants}
          className="header-content"
        >
          <h1 className="title">Bienvenido al Curso de Termodinámica</h1>
          <p className="subtitle">¡Explora el fascinante mundo de la termodinámica y domina sus conceptos clave!</p>
        </motion.div>
      </div>

      <motion.div
        className="course-overview"
        initial="initial"
        animate="animate"
        variants={textVariants}
      >
        <h2 className="section-title">¿Qué aprenderás en este curso?</h2>
        <p>En este emocionante viaje de aprendizaje, te sumergirás en los fundamentos de la termodinámica y desarrollarás una comprensión sólida de conceptos esenciales como:</p>
        <ul>
          <li>Diagramas de PVT, PT, VT y PV</li>
          <li>Calidad de mezclas y cómo afecta a las propiedades termodinámicas</li>
          <li>Entalpía y su relación con los procesos de transferencia de calor</li>
          <li>Calor latente y su papel en las transformaciones de fase</li>
          <li>Uso de la tabla de saturación para análisis de vapor y líquido</li>
        </ul>
      </motion.div>

      
    </div>
  );
}

export default HomePage;
