const API_URL = "http://127.0.0.1:5000/messages";

export const getMessages = async () => {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Failed to fetch messages");
        return await response.json();
    } catch (error) {
        console.error("Error fetching messages:", error);
        return { error: error.message };
    }
};

export const createMessage = async (messageData) => {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(messageData),
        });

        if (!response.ok) throw new Error("Failed to create message");
        return await response.json();
    } catch (error) {
        console.error("Error creating message:", error);
        return { error: error.message };
    }
};

export const updateMessage = async (id, messageData) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(messageData),
        });

        if (!response.ok) throw new Error("Failed to update message");
        return await response.json();
    } catch (error) {
        console.error("Error updating message:", error);
        return { error: error.message };
    }
};

export const deleteMessage = async (id) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
        if (!response.ok) throw new Error("Failed to delete message");
        return { success: true };
    } catch (error) {
        console.error("Error deleting message:", error);
        return { error: error.message };
    }
};