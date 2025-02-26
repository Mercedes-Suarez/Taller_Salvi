import {
    getChatMessages,
    getChatMessageById,
    createChatMessage,
    updateChatMessage,
    deleteChatMessage
} from "../services/chatmessagesService";

export const fetchChatMessages = async (setChatMessages) => {
    try {
        const data = await getChatMessages();
        if (data.error) {
            console.error("Error fetching messages:", data.error);
            return;
        }
        setChatMessages(data);
    } catch (error) {
        console.error("Error:", error);
    }
};

export const fetchChatMessageById = async (id, setChatMessage) => {
    try {
        const data = await getChatMessageById(id);
        setChatMessage(data);
    } catch (error) {
        console.error("Error:", error);
    }
};

export const addChatMessage = async (chatMessageData, setChatMessages) => {
    try {
        const response = await createChatMessage(chatMessageData);
        if (response.error) {
            console.error("Error adding message:", response.error);
            return;
        }
        fetchChatMessages(setChatMessages);
    } catch (error) {
        console.error("Error:", error);
    }
};

export const editChatMessage = async (id, chatMessageData, setChatMessages) => {
    try {
        const response = await updateChatMessage(id, chatMessageData);
        if (response.error) {
            console.error("Error updating message:", response.error);
            return;
        }
        fetchChatMessages(setChatMessages);
    } catch (error) {
        console.error("Error:", error);
    }
};

export const removeChatMessage = async (id, setChatMessages) => {
    try {
        const response = await deleteChatMessage(id);
        if (response.error) {
            console.error("Error deleting message:", response.error);
            return;
        }
        fetchChatMessages(setChatMessages);
    } catch (error) {
        console.error("Error:", error);
    }
};