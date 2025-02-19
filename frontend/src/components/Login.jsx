import React, { useState } from "react";
import { useUserHandler } from "../handler/AuthHandler";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import { CustomSweetAlertError, CustomSweetAlertOk } from "../components/CustomSweetAlert";
import { Button, InputGroup } from 'react-bootstrap';
import { FiLock, FiUnlock } from 'react-icons/fi';
import 'bootstrap/dist/css/bootstrap.min.css';


const Login = ({ showRegisterForm }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { handleLogin } = useUserHandler();

  const [showPassword, setShowPassword] = useState(false);

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const handleRegisterLinkClick = () => {
    showRegisterForm();
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await handleLogin(email, password);
      CustomSweetAlertOk('¡Login exitoso!').then(() => {
        setEmail("");
        setPassword("");
      });
    } catch (error) {
      console.log(error)
    }
  };

  return (
    <>
      <div className="d-flex justify-content-center  container-custom-register ">
        <Container className="card-custom p-4">
          <Container>
            <Row className="mt-5 mb-5 ">
              <Col lg={12} xl={6} md={12} >
                <p className="fw-bold mb-2">Area privada</p>
                <p className="fs-6">
                  Si no tienes cuenta {" "}
                  <a className="login-link" onClick={handleRegisterLinkClick}>
                    Regístrate pinchando aquí
                  </a>
                  .
                </p>
                <hr className="hr" />
                <form onSubmit={handleSubmit} style={{ marginTop: '150px' }}>
                  <label className="fw-bold" htmlFor="form2Example1">
                    EMAIL
                  </label>
                  <div className="form-outline mb-4">
                    {/* <input
                      type="email"
                      id="form2Example1"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      placeholder="Introduce tu email"
                    /> */}
                     <Form.Control className="pt-0 pb-0 pl-1 pr-0 border-1 rounded-0 bg-gray" style={{ borderColor: "#cccccc" }}
                        type="email"
                        id="form2Example1"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        placeholder="Introduce tu email"
                      />
                  </div>

                  <label className="fw-bold" htmlFor="form2Example2">CONTRASEÑA</label>
                  <div className="form-outline mb-4">
                  <InputGroup>
                      <Form.Control className="pt-0 pb-0 pl-1 pr-0 border-1 rounded-0 bg-gray " style={{ borderColor: "#cccccc" }}
                        type={showPassword ? 'text' : 'password'}
                        id="form2Example2"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        placeholder="Introduce tu contraseña"
                      />
                      <InputGroup.Text onClick={togglePasswordVisibility} style={{ cursor: 'pointer' }} className=" pt-0 pb-0 pl-1 pr-0 border-1 rounded-0 bg-gray ">
                        {showPassword ? <FiUnlock /> : <FiLock />}
                      </InputGroup.Text>
                    </InputGroup>
                  </div>


                  <Container className="mb-4 ms-0">
                    <Row className="row-checkbox">
                      <Col>
                        <Form.Group id="formGridCheckbox">
                          <Form.Check
                            type="checkbox"
                            label="Recordar contraseña"
                          />
                        </Form.Group>
                      </Col>
                      <Col>
                        <p className="fs-6">
                          {" "}
                          <a href="#" className="login-link">
                            Olvidé mi contraseña
                          </a>
                          .
                        </p>
                      </Col>
                    </Row>
                  </Container>
                  <button type="submit" className="btn-register p-1">
                    ENVIAR
                  </button>
                </form>
             </Col>
            </Row>
          </Container>
        </Container>
      </div>
    </>
  );
};

export default Login;