const API_URL = "http://127.0.0.1:5000/api/clients";

export const getclients = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getclientsById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};

export const createclients = async (clientsData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(clientsData),
    });
    return response.json();
};

export const updateclients = async (id, clientsData) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(clientsData),
    });
    return response.json();
};

export const deleteclients = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};