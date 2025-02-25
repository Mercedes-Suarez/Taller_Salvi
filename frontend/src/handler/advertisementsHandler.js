import {
    getAdvertisement,
    createAdvertisement,
    updateAdvertisements,
    deleteAdvertisements
} from "../services/advertisementsService";

export const fetchAdvertisement = async (setAdvertisement) => {
    const data = await getAdvertisement();
    setAdvertisement(data);
};

export const addAdvertisement = async (AdvertisementData, setAdvertisement) => {
    await createAdvertisement(AdvertisementData);
    fetchAdvertisement(setAdvertisement);
};

export const editAdvertisement = async (id, AdvertisementData, setAdvertisement) => {
    await updateAdvertisements(id, AdvertisementData);
    fetchAdvertisements(setAdvertisement);
};

export const removeAdvertisement = async (id, setAdvertisement) => {
    await deleteAdvertisement(id);
    fetchAdvertisement(setAdvertisement);
};