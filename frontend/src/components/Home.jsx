import React from "react";
import Carousel from "./Carousel";
import Services from "./Services";
import AboutMe from "./AboutMe";

const Home = () => {
  return (
    <div className="flex flex-col items-center w-full">
      {/* Carrusel de imágenes */}
      <Carousel />

      {/* Sección de Servicios */}
      <Services />

      {/* Sección "Sobre Mí" */}
      <AboutMe />

      {/* Aquí agregaremos Contact y Advertisement más adelante */}
      <div className="w-full min-h-[300px] flex items-center justify-center bg-gray-200 p-8">
        <h2 className="text-3xl font-bold">Aquí irá Contact y Advertisement</h2>
      </div>
    </div>
  );
};
  
  export default Home;