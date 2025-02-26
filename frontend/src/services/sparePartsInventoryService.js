const API_URL = "http://127.0.0.1:5000/spare_parts";

export const getSpareParts = async () => {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error("Failed to fetch spare parts");
        return await response.json();
    } catch (error) {
        console.error("Error fetching spare parts:", error);
        return { error: error.message, data: [] };
    }
};

export const getSparePartById = async (id) => {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        if (!response.ok) throw new Error("Failed to fetch spare part");
        return await response.json();
    } catch (error) {
        console.error("Error fetching spare part:", error);
        return { error: error.message };
    }
};

export const createSparePart = async (sparePartData) => {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(sparePartData),
        });

        if (!response.ok) throw new Error("Failed to create spare part");
        return await response.json();
    } catch (error) {
        console.error("Error creating spare part:", error);
        return { error: error.message };
    }
};

export const updateSparePart = async (id, sparePartData) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(sparePartData),
        });

        if (!response.ok) throw new Error("Failed to update spare part");
        return await response.json();
    } catch (error) {
        console.error("Error updating spare part:", error);
        return { error: error.message };
    }
};

export const deleteSparePart = async (id) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
        if (!response.ok) throw new Error("Failed to delete spare part");
        return { success: true };
    } catch (error) {
        console.error("Error deleting spare part:", error);
        return { error: error.message };
    }
};