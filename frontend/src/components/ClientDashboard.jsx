import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

const ClientDashboard = () => {
  // Simulación de datos de servicios
  const servicios = [
    {
      id: 1,
      titulo: "Cambio de aceite",
      estado: "En proceso",
      fecha: "2025-02-10",
    },
    {
      id: 2,
      titulo: "Revisión de frenos",
      estado: "Finalizado",
      fecha: "2025-01-20",
    },
  ];

  const solicitarServicio = () => {
    alert("Funcionalidad en desarrollo. ¡Próximamente podrás solicitar un servicio en línea!");
  };

  return (
    <Container className="mt-4">
      <h2>Bienvenido al Panel del Cliente</h2>
      <p>Aquí puedes ver el estado de tus servicios y solicitar nuevos.</p>
      
      <Row className="mt-4">
        {servicios.map((servicio) => (
          <Col key={servicio.id} md={6} lg={4} className="mb-4">
            <Card>
              <Card.Body>
                <Card.Title>{servicio.titulo}</Card.Title>
                <Card.Text>
                  Estado: <strong>{servicio.estado}</strong>
                </Card.Text>
                <Card.Text>
                  Fecha: {servicio.fecha}
                </Card.Text>
                <Button variant="primary" disabled={servicio.estado !== "Finalizado"}>
                  Ver Detalles
                </Button>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
      
      <Button onClick={solicitarServicio} variant="success" className="mt-3">
        Solicitar Nuevo Servicio
      </Button>
    </Container>
  );
};

export default ClientDashboard;