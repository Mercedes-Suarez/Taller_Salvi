import axios from "axios";
import {CustomSweetAlertError} from '../components/CustomSweetAlert'

const apiClient = axios.create({
    baseURL: 'http://localhost:5000',
    withCredentials: false,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
});

export const ContentService = {
    async getAllContent(userId) {
        try {
            let response = await apiClient.get(`/user_content/get_user_content/${userId}`);
            let allContent = response.data;
            return allContent;
        } catch (error) {
            console.error("Error getting the videos", error);
            CustomSweetAlertError("No se ha podido recuperar el contenido. Vuelva a intentarlo más tarde.");
            throw error;
        }
    },
    async updateStatusVideo(userId, contentId) {
        try {
            return await apiClient.patch(`/user_content/update_user_content/${userId}/${contentId}`);
        } catch (error) {
            console.error("Error updating status of the video:", error);
            CustomSweetAlertError("No se ha podido actualizar el estado del vídeo. Vuelva a intentarlo más tarde.");
            throw error;
        }
    },
    async updateNotes(userId, contentId, notes) {
        try {
            let response = await apiClient.patch(`/user_content/update_notes/${userId}/${contentId}`, { notes });
            return response.data;
        } catch (error) {
            console.error("Error updating notes:", error);
            CustomSweetAlertError("No se ha podido actualizar las notas. Vuelva a intentarlo más tarde.");
            throw error;
        }
    }
    
};

export default ContentService;