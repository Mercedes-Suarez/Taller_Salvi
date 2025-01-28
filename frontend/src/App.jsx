import { BrowserRouter } from 'react-router-dom';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
//import { createBrowserRouter, RouterProvider } from 'react-router-dom';


//const router = createBrowserRouter ([
//  {path: "/", element: <div>Bienvenido a Taller Salvi</div>},
//  {path: "/about_me", element: <div>Sobre mí</div>},
//  {path: "/services", element: <div>Servicios</div>},
//  {path: "/contact", element: <div>Contacto</div>},
 // {path: "/private_area", element: <div>Area Privada</div>},
  //{path: "/register", element: <div>Regístrate</div>},
  //{path: "/logout", element: <div>Exit </div>},


//]);

function App() {
  
  return (

      <BrowserRouter
        future={{v7_startTransition: true }}>
      
        <Navbar />
        <Routes>
        <Route path="/" element={<div>Bienvenido a Taller Salvi</div>} />
        <Route path="/about_me" element={<div>Sobre mí</div>} />
        <Route path="/services" element={<div>Servicios</div>} />
        <Route path="/contact" element={<div>Contacto</div>} />
        <Route path="/private_area" element={<div>Área Privada</div>} />
        <Route path="/register" element={<div>Regístrate</div>} />
        <Route path="/logout" element={<div>Exit</div>} />
      </Routes>
      
      </BrowserRouter>

  );
       
} 

export default App;
