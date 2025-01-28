import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container">
        <Link className="navbar-brand text-white" to="/">Taller Salvi</Link>
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

//import React from "react";
//import { Link } from "react-router-dom";

//function Navbar() {
   // return(


     //   <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
    //    <div className="container">
   //       <Link className="navbar-brand" to="/">Taller Salvi</Link>
   //       <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
     //       <span className="navbar-toggler-icon"></span>
    //      </button>
    //      <div className="collapse navbar-collapse" id="navbarNav">
    //        <ul className="navbar-nav ms-auto">
    //          <li className="nav-item"><Link className="nav-link" to="/">Inicio</Link></li>
   //           <li className="nav-item"><Link className="nav-link" to="/about_me">Sobre mí</Link></li>
   //           <li className="nav-item"><Link className="nav-link" to="/services">Servicios</Link></li>
    //          <li className="nav-item"><Link className="nav-link" to="/contact">Contacto</Link></li>
    //          <li className="nav-item"><Link className="nav-link" to="/login">Area Privada</Link></li>
    //          <li className="nav-item"><Link className="nav-link" to="/logout">Salir</Link></li>
    //        </ul>
    //      </div>
   //     </div>
  //    </nav>
 //   );
    
//}

//export default Navbar;

