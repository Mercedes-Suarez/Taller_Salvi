const API_URL = "http://127.0.0.1:5000/api/advertisements";

export const getAdvertisement = async () => {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`Failed to fetch advertisements (${response.status})`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching advertisements:", error);
        return { error: error.message, data: [] };  // ✅ Devuelve un objeto en vez de un array vacío
    }
};

export const createAdvertisement = async (advertisementData) => {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(advertisementData),
        });

        if (!response.ok) {
            const errorResponse = await response.json();
            throw new Error(errorResponse.error || "Failed to create advertisement");
        }

        return await response.json();
    } catch (error) {
        console.error("Error creating advertisement:", error);
        return { error: error.message };
    }
};

export const updateAdvertisement = async (id, advertisementData) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(advertisementData),
        });

        if (!response.ok) {
            const errorResponse = await response.json();
            throw new Error(errorResponse.error || "Failed to update advertisement");
        }

        return await response.json();
    } catch (error) {
        console.error("Error updating advertisement:", error);
        return { error: error.message };
    }
};

export const deleteAdvertisement = async (id) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });

        if (!response.ok) throw new Error("Failed to delete advertisement");

        return { success: true };
    } catch (error) {
        console.error("Error deleting advertisement:", error);
        return { error: "Failed to delete advertisement" };
    }
};