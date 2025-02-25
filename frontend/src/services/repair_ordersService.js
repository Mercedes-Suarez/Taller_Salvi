const API_URL = "http://127.0.0.1:5000/api/repair_orders";

export const getRepair_orders = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getRepair_ordersById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};

export const createRepair_orders = async (repair_ordersData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(repair_ordersData),
    });
    return response.json();
};

export const deleteRepair_orders = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};