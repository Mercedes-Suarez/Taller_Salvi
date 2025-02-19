import axios from "axios";
import { jwtDecode } from 'jwt-decode';


function setCookie(name, value, days, minutes) {
  let expires = "";
  if (days) {
    let date = new Date();
    date.setTime(date.getTime() + (minutes * 60 * 1000));
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

export const loginUser = async (email, password,user_type) => {

  try {
    const url = "http://127.0.0.1:5000/login/";
    const userData = {
      email: email,
      password: password,
      user_type: user_type
    };

    const response = await axios.post(url, userData);

    if (response.status === 200 && response.data) {
      console.log("Usuario autenticado con éxito:", response.data);

      const token = response.data.token;
      const decodedToken = jwtDecode(token);
      console.log(decodedToken)
      setCookie ("id_user",decodedToken.id_user);
      setCookie ("name", decodedToken.name);
      setCookie ("surname", decodedToken.surname);
      // setCookie ("password", decodedToken.password);
      setCookie ("email", decodedToken.email);
      setCookie ("phone", decodedToken.phone);
      setCookie ("photo", decodedToken.photo);
      setCookie ("user_type", decodedToken.user_type);

      console.log("Token decodificado:", decodedToken);

      const user_type = decodedToken.user_type;
      console.log("Tipo de rol del usuario:", user_type);

      return { success: true, userId: decodedToken.id_user, user_type: user_type};
    } else {
      console.error("Error al autenticar al usuario:", response.statusText);
      return { success: false };
    }
  } catch (error) {
    console.error("Error al realizar la solicitud:", error);
    return { success: false };
  }

};

export default loginUser;