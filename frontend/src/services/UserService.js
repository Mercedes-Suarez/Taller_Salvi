import axios from "axios";
import {CustomSweetAlertError} from '../components/CustomSweetAlert'


const apiClient = axios.create({
    baseURL: "http://127.0.0.1:5000",
    withCredentials: false,
    headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
    },
});
export const UserService = {
    async getUser() {
        try {
            let response = await apiClient.get("/user_admin/get_user");
            let allUsers = response.data;
            return allUsers;
        } catch (error) {
            console.error("Error al obtener los usuarios:", error);
        }
    },
    async postUser(newUser) {
        try {
            const response = await apiClient.post("/user_client/post_user", newUser);
            // Si la respuesta incluye 'Email or password already exists', rechaza la promesa con un mensaje personalizado
            if (response.data.includes('Email or password already exists')) {
                throw new Error('El correo electrónico ya existe.');
            }
            return response;
        } catch (error) {
            console.error("Error al enviar el usuario:", error);
            throw error; // Lanza el error para ser manejado por el llamador
        }
    },
    
    async updateUser(id, updatedUser) {
        try {
            return await apiClient.patch(
                `/user_client/update_user/${id}`,
                updatedUser
            );
        } catch (error) {
            console.error("Error updating user:", error);
            throw error;
        }
    },
    async deleteUserProfile(id) {
        try {
            return await apiClient.delete(`/user_client/delete_user/${id}`);
        } catch (error) {
            console.error("Error al eliminar el usuario:", error);
            CustomSweetAlertError("Hubo un error al eliminar el usuario. Por favor, intente nuevamente más tarde.");
            throw error;
        }
    },
    
    async getAlltUsers() {
        try {
            let response = await apiClient.get("/user_client/get_user");
            let allUsers = response.data;
            return allUsers;
        } catch (error) {
            console.error("Error al obtener los usuarios:", error);
        }
    },
};
export default UserService;