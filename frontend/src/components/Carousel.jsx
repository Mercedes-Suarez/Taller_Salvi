import React from 'react';
import { Swiper, SwiperSlide } from "swiper/react";
import { Autoplay, Pagination, Navigation } from "swiper/modules";
import { motion } from "framer-motion";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import img01_carousel from "/src/assets/img01_carousel.jpg";
import img02_carousel from "/src/assets/img02_carousel.jpg";
import img03_carousel from "/src/assets/img03_carousel.jpg";
import img04_carousel from "/src/assets/img04_carousel.jpg";
import img05_carousel from "/src/assets/img05_carousel.jpg";
import img06_carousel from "/src/assets/img06_carousel.jpg";
import img07_carousel from "/src/assets/img07_carousel.jpg";
import img08_carousel from "/src/assets/img08_carousel.jpg";

const images = [
  { src: img01_carousel, text: "Bienvenido." },
  { src: img02_carousel, text: "¿Que le ocurre al coche?" },
  { src: img03_carousel, text: "Tu coche necesita..." },
  { src: img04_carousel, text: "A reparar." },
  { src: img05_carousel, text: "Comprobando reparación." },
  { src: img06_carousel, text: "Lo comprueba el cliente" },
  { src: img07_carousel, text: "Verificado, todo correcto." },
  { src: img08_carousel, text: "Gracias por tu confianza"}
];

const Carousel = () => {
  return (
    <div className="w-full h-[600px] overflow-hidden">
      <Swiper
        spaceBetween={0}
        centeredSlides={true}
        autoplay={{ delay: 3000, disableOnInteraction: false }}
        pagination={{ clickable: true }}
        navigation={true}
        modules={[Autoplay, Pagination, Navigation]}
        className="h-[600px] w-full min-h-[600px]"
      >
        {images.map((item, index) => {
          console.log(item.src);
          return (
          <SwiperSlide key={index} className="relative">
            <img
              src={item.src}
              alt={`Slide ${index + 1}`}
              className="w-full h-full object-cover"
            />            
            <motion.div
              className="absolute inset-0 flex items-center justify-center bg-black bg-opacity-40"
              initial={{ opacity: 0, y: 50 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8 }}
            >
              <motion.h2
                className="text-white text-3xl font-bold"
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 1, delay: 0.3 }}
              >
                {item.text}
              </motion.h2>
            </motion.div>
            </SwiperSlide>
          );
        })}
      </Swiper>
    </div>
);
};

export default Carousel;