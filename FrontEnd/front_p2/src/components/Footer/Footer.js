import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section">
          <h3>Acerca de Nosotros</h3>
          <p>Somos una plataforma de aprendizaje en línea dedicada a la enseñanza de la termodinámica y conceptos relacionados.</p>
        </div>

        <div className="footer-section">
          <h3>Síguenos en Redes Sociales</h3>
          <div className="social-icons">
            <a href="#" target="_blank" rel="noopener noreferrer">
              <img src="/facebook-icon.png" alt="Facebook" />
            </a>
            <a href="#" target="_blank" rel="noopener noreferrer">
              <img src="/twitter-icon.png" alt="Twitter" />
            </a>
            <a href="#" target="_blank" rel="noopener noreferrer">
              <img src="/instagram-icon.png" alt="Instagram" />
            </a>
          </div>
        </div>

        <div className="footer-section">
          <h3>Contacto</h3>
          <p>Si tienes alguna pregunta o comentario, no dudes en contactarnos:</p>
          <p>Email: <a href="mailto:info@example.com">info@example.com</a></p>
          <p>Teléfono: <a href="tel:+123456789">+123456789</a></p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
