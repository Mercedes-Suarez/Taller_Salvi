import React from "react";

const AboutMe = () => {
  return (
    <section className="w-full min-h-[400px] bg-blue-500 flex items-center justify-center p-8">
      <div className="max-w-6xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
        <h2 className="text-4xl md:text-5xl font-bold text-black text-left">
          Sobre mí
        </h2>
        <p className="text-white text-lg text-right">
          Taller Salvi cuenta con más de 10 años de experiencia en la reparación de vehículos. 
          Nos especializo en mecánica general, electricidad, garantizando 
          la máxima calidad y satisfacción para mis clientes.
        </p>
      </div>
    </section>
  );
};

export default AboutMe;