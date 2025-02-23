const API_URL = "http://127.0.0.1:5000/api/vehicles";

export const getVehicles = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getVehicleById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};

export const createVehicle = async (vehicleData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(vehicleData),
    });
    return response.json();
};

export const updateVehicle = async (id, vehicleData) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(vehicleData),
    });
    return response.json();
};

export const deleteVehicle = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};