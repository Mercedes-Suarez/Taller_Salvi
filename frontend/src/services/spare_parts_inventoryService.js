const API_URL = "http://127.0.0.1:5000/api/spare_parts_inventory";

export const getSpareParts = async () => {
    const response = await fetch(API_URL);
    return response.json();
};
export const getSparePartsById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};


export const createSpareParts = async (sparePartsData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(sparePartsData),
    });
    return response.json();
};

export const updateSpareParts = async (id, sparePartsData) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(sparePartsData),
    });
    return response.json();
};

export const deleteSpareParts = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};