import {
    getMessages,
    createMessage,
    updateMessage,
    deleteMessage
} from "../services/messagesService";

export const fetchMessages = async (setMessages) => {
    try {
        const data = await getMessages();
        if (data.error) {
            console.error("Error fetching messages:", data.error);
            return;
        }
        setMessages(data);
    } catch (error) {
        console.error("Error:", error);
    }
};

export const addMessage = async (messageData, setMessages) => {
    try {
        const response = await createMessage(messageData);
        if (response.error) {
            console.error("Error adding message:", response.error);
            return;
        }
        fetchMessages(setMessages);
    } catch (error) {
        console.error("Error:", error);
    }
};

export const editMessage = async (id, messageData, setMessages) => {
    try {
        const response = await updateMessage(id, messageData);
        if (response.error) {
            console.error("Error updating message:", response.error);
            return;
        }
        fetchMessages(setMessages);
    } catch (error) {
        console.error("Error:", error);
    }
};

export const removeMessage = async (id, setMessages) => {
    try {
        const response = await deleteMessage(id);
        if (response.error) {
            console.error("Error deleting message:", response.error);
            return;
        }
        fetchMessages(setMessages);
    } catch (error) {
        console.error("Error:", error);
    }
};