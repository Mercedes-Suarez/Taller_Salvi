import ContentService from "../services/ContentService";


export const ContentHandler = {
    async getAllContent(userId) {

       try {
            let content = await ContentService.getAllContent(userId);
            return content;
        } catch (error) {
            console.error("Error getting the videos", error);
            throw error; 
        }
    },
    async updateStatusVideo(userId, contentId) {
        try {
            return await ContentService.updateStatusVideo(userId, contentId);
        } catch (error) {
            console.error("Error updating video status:", error);
            throw error;
        }
    },
    async updateNotes(userId, contentId, notes) {
        try {
            return await ContentService.updateNotes(userId, contentId, notes);
        } catch (error) {
            console.error("Error updating notes:", error);
            throw error;
        }
    }
};

export default ContentHandler;