import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import './NavBar.css';
function NavBar() {
  return (
    <nav className="navbar">
      <Link to="/" className="navbar-brand">
        App Name
      </Link>
      <ul className="navbar-nav">
        <li className="nav-item">
          <NavLink to="/about" className="nav-link" activeClassName="active">
            About
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink to="/help" className="nav-link" activeClassName="active">
            Help
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink to="/account" className="nav-link" activeClassName="active">
            Account
          </NavLink>
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;
