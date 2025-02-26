const API_URL = "http://127.0.0.1:5000/session_tokens";

export const getSessionTokens = async () => {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Failed to fetch session tokens");
        return await response.json();
    } catch (error) {
        console.error("Error fetching session tokens:", error);
        return { error: error.message };
    }
};

export const createSessionToken = async (sessionTokenData) => {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(sessionTokenData),
        });

        if (!response.ok) throw new Error("Failed to create session token");
        return await response.json();
    } catch (error) {
        console.error("Error creating session token:", error);
        return { error: error.message };
    }
};

export const updateSessionToken = async (id, sessionTokenData) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(sessionTokenData),
        });

        if (!response.ok) throw new Error("Failed to update session token");
        return await response.json();
    } catch (error) {
        console.error("Error updating session token:", error);
        return { error: error.message };
    }
};

export const deleteSessionToken = async (id) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
        if (!response.ok) throw new Error("Failed to delete session token");
    } catch (error) {
        console.error("Error deleting session token:", error);
    }
};