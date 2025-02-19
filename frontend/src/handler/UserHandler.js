import UserService from '../services/UserService';
import {CustomSweetAlertError} from '../components/CustomSweetAlert'

export const UserHandler = {
    async getUser() {
        let user = await UserService.getUser();
        return user;
    },
    async getAlltUsers() {
        let allUsers = await UserService.getAlltUsers();
        return allUsers;
    },
    async postUser(newUser) {
        return UserService.postUser(newUser).then((response) => {
            if (response.status === 200) {
                console.log(response.data);
            } else {
                throw new Error('Error al enviar el usuario');
            }
        });
    },
    async updateUser(id, updatedUser) {
        try {
            return await UserService.updateUser(id, updatedUser);
        } catch (error) {
            console.error("Error al actualizar usuario:", error);
            throw error;
        }
    },
    async handleDeleteUserProfile(id) {
        try {
            await UserService.deleteUserProfile(id);
            console.log("Usuario eliminado exitosamente");
        } catch (error) {
            console.error("Error al manejar la eliminación del usuario:", error);
            CustomSweetAlertError("Hubo un error al eliminar el usuario. Por favor, intente nuevamente más tarde.");
            throw error;
        }
    }
}
export default UserHandler;