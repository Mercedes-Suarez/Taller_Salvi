const API_URL = "http://127.0.0.1:5000/api/messages";

export const getMessages = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const createMessage = async (messageData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(messageData),
    });
    return response.json();
};

export const updateMessage = async (id, messageData) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(messageData),
    });
    return response.json();
};

export const deleteMessage = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};