import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo_android_chrome_192x192.png";

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container">
        <Link className="navbar-logo" to="/">
          <img src= {logo} alt="Logo Taller Salvi" className="h-16 w-auto" />
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item"><Link className="nav-link text-black" to="/">Inicio</Link></li>
            <li className="nav-item"><Link className="nav-link text-black" to="/about_me">Sobre mí</Link></li>
            <li className="nav-item"><Link className="nav-link text-black" to="/services">Servicios</Link></li>
            <li className="nav-item"><Link className="nav-link text-black" to="/contact">Contacto</Link></li>
            <li className="nav-item"><Link className="nav-link text-black" to="/private_area">Área Privada</Link></li>
            <li className="nav-item"><Link className="nav-link text-black" to="/logout">Salir</Link></li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;