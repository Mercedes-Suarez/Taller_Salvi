import React from "react";
import { Routes, Route, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import { jwtDecode } from 'jwt-decode';

import Navbar from './components/Navbar';
import AboutMe from './components/AboutMe';
import Footer from './components/Footer';
import Home from './components/Home';
//import Contact from './components/Contact';
import FormRegister from './components/FormRegister';
import Login from './components/Login';
import AdminDashboard from './components/AdminDashboard';
import ClientDashboard from './components/ClientDashboard';
import Services from './components/Services';
import Logout from './components/Logout';


function App() {
  
  const navigate = useNavigate();

  // Verificación del Token al Inicio
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      try {
        const decodedToken = jwtDecode(token);
        const currentTime = Math.floor(Date.now() / 1000);

        if (decodedToken.exp < currentTime) {
          // Token expirado, redirige al login y remueve el token
          localStorage.removeItem("token");
          navigate('/login');
        } else {
          // Token válido, redirige al dashboard según el rol
          if (decodedToken.user_type === 'admin') {
            navigate('/admin/dashboard');
          } else if (decodedToken.user_type === 'client') {
            navigate('/client/dashboard');
          }
        }
      } catch (error) {
        console.error("Token inválido", error);
        localStorage.removeItem("token");
        navigate('/login');
      }
    }
  }, [navigate]);

  return (

      <>

        <Navbar />

        <Routes>
          <Route path="/" element={<Home />} />
          
          <Route path="/register" element={<FormRegister />} />
          <Route path="/login" element={<Login />} />
          <Route path="/admin/dashboard" element={<AdminDashboard />} />
          <Route path="/client/dashboard" element={<ClientDashboard />} />
          <Route path="/navbar" element={<Navbar />}/>
          <Route path="/about_me" element={<AboutMe />} />
          <Route path="/services" element={<Services />} />
          <Route path="/footer" element={<Footer />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>

        <Footer />
      </>

  );
       
} 

export default App;
