const API_URL = "http://127.0.0.1:5000/user_types";

export const getUserTypes = async () => {
    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`Error fetching user types (${response.status})`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching user types:", error);
        return { error: error.message, data: [] };
    }
};

export const createUserType = async (userTypeData) => {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userTypeData),
        });

        if (!response.ok) {
            const errorResponse = await response.json();
            throw new Error(errorResponse.error || "Failed to create user type");
        }

        return await response.json();
    } catch (error) {
        console.error("Error creating user type:", error);
        return { error: error.message };
    }
};

export const updateUserType = async (id, userTypeData) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userTypeData),
        });

        if (!response.ok) {
            const errorResponse = await response.json();
            throw new Error(errorResponse.error || "Failed to update user type");
        }

        return await response.json();
    } catch (error) {
        console.error("Error updating user type:", error);
        return { error: error.message };
    }
};

export const deleteUserType = async (id) => {
    try {
        const response = await fetch(`${API_URL}/${id}`, { method: "DELETE" });

        if (!response.ok) throw new Error("Failed to delete user type");

        return { success: true };
    } catch (error) {
        console.error("Error deleting user type:", error);
        return { error: "Failed to delete user type" };
    }
};