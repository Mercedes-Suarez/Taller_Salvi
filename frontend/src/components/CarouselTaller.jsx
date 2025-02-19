import React from 'react';
import './history.css'
import Carousel from 'react-bootstrap/Carousel';
import history from '../../assets/img/history1.jpg'
import history2 from '../../assets/img/history2.jpg';
import history3 from '../../assets/img/history3.jpg';

const History = () => {
  return (
    <>
    <section className='componenthistory'>
      <Carousel>
      <Carousel.Item>
        <img className='history1' src={history} alt='Deportista haciendo plancha lateral' />
        <Carousel.Caption>
          <h2 className='caption-title'>BREVE HISTORIA</h2>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img className='history2' src={history2} alt='Nadador' />
        <Carousel.Caption>
          <h2 className='caption-title'>TRATAMIENTO INDIVIDUAL</h2>
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img className='history3' src={history3} alt='Hombre haciendo Motocross' />
        <Carousel.Caption>
          <h2 className='caption-title'>SI QUIERES CAMBIAR HAZLO DESDE DENTRO</h2>
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
    </section>
    </>
  )
}

export default History;