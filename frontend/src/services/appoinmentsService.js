const API_URL = "http://127.0.0.1:5000/api/appoinments";

export const getappoinments = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const createappoinments = async (appoinmentsData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(appoinmentsData),
    });
    return response.json();
};

export const updateappoinments = async (id, appoinmentsData) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(appoinmentsData),
    });
    return response.json();
};

export const deleteappoinments = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};