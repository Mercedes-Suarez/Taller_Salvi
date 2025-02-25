const API_URL = "http://127.0.0.1:5000/api/advertisements";

export const getAdvertisement = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const createAdvertisement = async (AdvertisementsData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(AdvertisementsData),
    });
    return response.json();
};

export const updateAdvertisement = async (id, AdvertisementsData) => {
    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(AdvertisementsData),
    });
    return response.json();
};

export const deleteAdvertisement = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};