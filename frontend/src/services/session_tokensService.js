const API_URL = "http://127.0.0.1:5000/api/session_tokens";

export const getsession_tokens = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const createsession_tokens = async (session_tokensData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(session_tokensData),
    });
    return response.json();
};

export const updatesession_tokens = async (id, session_tokensData) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(session_tokensData),
    });
    return response.json();
};

export const deletesession_tokens = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};