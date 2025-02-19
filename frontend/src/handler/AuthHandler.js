import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import  loginUser  from '../services/AuthService';
import { CustomSweetAlertError, CustomSweetAlertOk} from '../components/CustomSweetAlert';

export const useUserHandler = () => {
 const [userType, setUserType] = useState(null);
 const navigate = useNavigate(); 

 const handleLogin = async (email, password,user_type) => {
    const response = await loginUser(email, password,user_type);
    if (response.success) {
      setUserType(response.user_type);

      localStorage.setItem("token", response.token);

      switch (response.user_type) {
         case 'admin' :
            navigate('/admin/dashboard');
         break;
         case  'client':
            navigate('/client/dashboard'); 
         break;
        default:

          break;
      }
    } else {
      CustomSweetAlertError('Error en el inicio de sesión.');
    }
 };

 return { handleLogin };
};

export default useUserHandler;