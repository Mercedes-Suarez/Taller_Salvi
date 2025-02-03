import React from "react";

const Services = () => {
  return (
    <section className="w-full min-h-[400px] bg-yellow-400 flex items-center justify-center p-8">
      <div className="max-w-6xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
        <h2 className="text-4xl md:text-5xl font-bold text-black text-left">
          Servicios
        </h2>
        <p className="text-black text-lg text-right">
          Ofrecemos una amplia gama de servicios, incluyendo:
          <ul className="list-disc list-inside mt-2">
            <li>Revisión y mantenimiento general.</li>
            <li>Diagnóstico y reparación de motores.</li>
            <li>Servicio de frenos y suspensión.</li>
            <li>Chapa y pintura.</li>
            <li>Electromecánica y diagnosis avanzada.</li>
          </ul>
        </p>
      </div>
    </section>
  );
};

export default Services;