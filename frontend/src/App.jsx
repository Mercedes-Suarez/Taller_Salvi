import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Carousel from './components/Carousel';
import AboutMe from './components/AboutMe';
import Services from './components/Services';

function App() {
  
  return (

      <BrowserRouter
        future={{v7_startTransition: true }}>
      
        <Navbar />

        <Routes>
        <Route path="/about_me" element={<AboutMe />} />
        <Route path="/services" element={<Services />} />
        <Route path="/contact" element={<div>Contacto</div>} />
        <Route path="/private_area" element={<div>Área Privada</div>} />
        <Route path="/register" element={<div>Regístrate</div>} />
        <Route path="/logout" element={<div>Exit</div>} />
      </Routes>

        <Carousel />
        <AboutMe />
        <Services />

      </BrowserRouter>

  );
       
} 

export default App;
