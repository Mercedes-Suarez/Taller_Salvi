import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  useEffect(() => {
    // Remueve el token y redirige al Home
    localStorage.removeItem("token");
    navigate('/');
  }, [navigate]);

  return <div>Cerrando sesión...</div>;
};

export default Logout;