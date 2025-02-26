const API_URL = "http://127.0.0.1:5000/chat_messages";

export const getChatMessages = async () => {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Failed to fetch messages");
        return await response.json();
    } catch (error) {
        console.error("Error fetching messages:", error);
        return { error: error.message };
    }
};

export const getChatMessageById = async (id) => {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        if (!response.ok) throw new Error("Message not found");
        return await response.json();
    } catch (error) {
        console.error("Error fetching message:", error);
        return { error: error.message };
    }
};

export const createChatMessage = async (chatMessageData) => {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(chatMessageData),
        });

        if (!response.ok) throw new Error("Failed to create message");
        return await response.json();
    } catch (error) {
        console.error("Error creating message:", error);
        return { error: error.message };
    }
};

export const updateChatMessage = async (id, chatMessageData) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(chatMessageData),
        });

        if (!response.ok) throw new Error("Failed to update message");
        return await response.json();
    } catch (error) {
        console.error("Error updating message:", error);
        return { error: error.message };
    }
};

export const deleteChatMessage = async (id) => {
    try {
        await fetch(`${API_URL}/${id}`, { method: "DELETE" });
        return { success: true };
    } catch (error) {
        console.error("Error deleting message:", error);
        return { error: error.message };
    }
};
