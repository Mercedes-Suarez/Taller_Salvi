const API_URL = "http://127.0.0.1:5000/api/repair_details";

export const getRepair_details = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getRepair_detailsById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};

export const createRepair_details = async (repair_detailsData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(repair_detailsData),
    });
    return response.json();
};

export const deleteRepair_details = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};
