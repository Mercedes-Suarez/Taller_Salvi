import {
    getAdvertisement,
    createAdvertisement,
    updateAdvertisement,
    deleteAdvertisement
} from "../services/advertisementsService";

export const fetchAdvertisements = async (setAdvertisements) => {
    const data = await getAdvertisement();
    if (data.error) {
        console.error("Error fetching advertisements:", data.error);
        return;  // No actualizar estado si hay error
    }
    setAdvertisements(data);
};

export const addAdvertisement = async (advertisementData, setAdvertisements) => {
    const response = await createAdvertisement(advertisementData);
    if (response.error) {
        console.error("Error adding advertisement:", response.error);
        return;  // ❌ Evitar actualizar si hay error
    }
    fetchAdvertisements(setAdvertisements);
};

export const editAdvertisement = async (id, advertisementData, setAdvertisements) => {
    const response = await updateAdvertisement(id, advertisementData);
    if (response.error) {
        console.error("Error updating advertisement:", response.error);
        return;
    }
    fetchAdvertisements(setAdvertisements);
};

export const removeAdvertisement = async (id, setAdvertisements) => {
    const response = await deleteAdvertisement(id);
    if (response.error) {
        console.error("Error deleting advertisement:", response.error);
        return;
    }
    fetchAdvertisements(setAdvertisements);
};