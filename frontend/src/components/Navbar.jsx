import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo_taller_salvi.png";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container">
        <Link className="navbar-logo" to="/">
          <img src= {logo} alt="Logo Taller Salvi" className="navbar-logo" />
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item"><Link className="nav-link text-white" to="/">Inicio</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/about_me">Sobre mí</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/services">Servicios</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/contact">Contacto</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/login">Área Privada</Link></li>
            <li className="nav-item"><Link className="nav-link text-white" to="/logout">Salir</Link></li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;