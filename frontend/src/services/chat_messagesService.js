const API_URL = "http://127.0.0.1:5000/api/chat_messages";

export const getchat_Messages = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getchat_MessagesById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};


export const createchat_Message = async (chat_messageData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(chat_messageData),
    });
    return response.json();
};

export const updatechat_Message = async (id, chat_messageData) => {
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