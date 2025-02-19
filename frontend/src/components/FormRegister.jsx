import { UserHandler } from "../handler/UserHandler";
import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
//import "./register.css";
//import register from "../../assets/img/register.svg";
import { CustomSweetAlertOk, CustomSweetAlertError } from "../components/CustomSweetAlert";

const FormRegister = ({ showLoginForm }) => {
  const [userName, setuserName] = useState("");
  const [surname, setSurname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [phone, setPhone] = useState("");
  const [selectedFile, setSelectedFile] = useState(null);
  const [repeatPassword, setRepeatPassword] = useState('');
  const [termsAccepted, setTermsAccepted] = useState(false);

  const handleLoginClick = () => {
    showLoginForm();
  };


  const handleSubmit = async (event) => {
    event.preventDefault();

    let isValid = true;

    if (password !== repeatPassword) {
      CustomSweetAlertError('Las contraseñas no coinciden');
      return; 
    }
    if (!userName || !surname || !email || !password || !phone) {
      isValid = false;
      CustomSweetAlertError('Debes completar todos los campos');
      return;
    }
    if (!termsAccepted) {
      CustomSweetAlertError('Debes aceptar términos y condiciones');
      return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      isValid = false;
      CustomSweetAlertError('Debes ingresar un email álido');
      return;
    }
    if (password.length < 8) {
      isValid = false;
      CustomSweetAlertError('La contraseña debe tener al menos 8 caracteres');
      return;
    }
    if (phone.length < 8) {
      isValid = false;
      CustomSweetAlertError('El teléfono debe contener al menos 8 números');
      return;
    }
    const formObject = {
      name: userName,
      surname: surname,
      email: email,
      password: password,
      phone: phone,
      photo: selectedFile ? URL.createObjectURL(selectedFile) : null,
      user_typeFK: 2,
    };

    try {
      await UserHandler.postUser(formObject);
      CustomSweetAlertOk('¡Felicidades, ya eres miembro de Inner Visuals!');
      resetForm();
    } catch (error) {
      console.error(error);
      CustomSweetAlertError('Hubo un error al crear el usuario');
    }
  };

  const resetForm = () => {
    setuserName ("");
    setSurname("");
    setEmail(""); 
    setPassword(""); 
    setPhone(""); 
    setSelectedFile(null);
    setRepeatPassword("");
  };

  return (
    <>
      <section className="login-register">
        <div className="d-flex justify-content-center container-custom-register ">
          <Container className="card-custom p-4">
            <Row className="mt-5">
              <Col lg={12} xl={6} md={12}>
                <p className="fw-bold">CREA TU CUENTA</p>
                <p className="fs-6">
                  Si ya tienes cuenta{" "}
                  <a className="login-link" onClick={handleLoginClick}>
                    loguéate pinchando aquí
                  </a>
                  .
                </p>
                <hr className="hr" />
                <form onSubmit={handleSubmit}>
                  <div className="form-outline mb-4">
                    <p className="fw-bold">Nombre</p>
                    <input
                      type="text"
                      id="form2Example1"
                      name="name"
                      value={userName}
                      onChange={(e) => setuserName(e.target.value)}
                      placeholder="Introduce tu nombre"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <p className="fw-bold" htmlFor="form2Example2">
                      Apellido
                    </p>
                    <input
                      type="text"
                      id="form2Example2"
                      name="surname"
                      value={surname}
                      onChange={(e) => setSurname(e.target.value)}
                      placeholder="Introduce tu apellido"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <p className="fw-bold" htmlFor="form2Example3">
                      Teléfono
                    </p>
                    <input
                      type="text"
                      id="form2Example3"
                      name="phone"
                      value={phone}
                      onChange={(e) => setPhone(e.target.value)}
                      placeholder="Introduce tu teléfono"
                    />
                  </div>
                  <div className="form-outline mb-4">
                    <Form.Group controlId="formFile" className="mb-3">
                      <p className="fw-bold">Foto</p>
                      <Form.Control
                        type="file"
                        className="input-field rounded-0 border-black "
                        onChange={(e) => setSelectedFile(e.target.files[0])}
                      />
                    </Form.Group>
                  </div>
                  <div className="form-outline mb-4">
                    <p className="fw-bold">Email</p>
                    <input
                      type="email"
                      id="form2Example4"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      placeholder="Introduce tu email"
                    />
                  </div>
                  <Container className="d-flex justify-content-between mb-4">
                    <Row>
                      <Col>
                        <p className="fw-bold">Contraseña</p>
                        <input
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          type="password"
                          id="inputPassword5"
                          aria-describedby="passwordHelpBlock"
                          placeholder="Introduce tu contraseña"
                        />
                      </Col>
                      <Col>
                        <p className="fw-bold"> Contraseña</p>
                        <input
                          value={repeatPassword}
                          onChange={(e) => setRepeatPassword(e.target.value)}
                          type="password"
                          
                          aria-describedby="passwordHelpBlocka"
                          placeholder="Repetir contraseña"
                        />
                      </Col>
                    </Row>
                  </Container>
                  <Form.Group className="mb-3 ms-2" controlId="termsCheckbox">
                    <Form.Check
                      type="checkbox"
                      label="Acepto los términos y condiciones"
                      onChange={() => setTermsAccepted(!termsAccepted)}
                    />
                  </Form.Group>
                  <Col className="d-flex justify-content-center mb-4">
                    <button className="btn-register p-1" type="submit">
                      ENVIAR
                    </button>
                  </Col>
                </form>
              </Col>
            
            </Row>
          </Container>
        </div>
      </section>
    </>
  );
};

export default FormRegister;
