import {
    getSpareParts,
    createSparePart,
    updateSparePart,
    deleteSparePart
} from "../services/spare_Parts_inventoryService";

export const fetchSpareParts = async (setSpareParts) => {
    const data = await getSpareParts();
    setSpareParts(data);
};

export const addSpareParts = async (sparePartsData, setSpareParts) => {
    await createSparePart(sparePartsData);
    fetchSpareParts(setSpareParts);
};

export const editSpareParts = async (id, sparePartsData, setSpareParts) => {
    await updateSparePart(id, sparePartsData);
    fetchSpareParts(setSpareParts);
};

export const removeSpareParts = async (id, setSpareParts) => {
    await deleteSparePart(id);
    fetchSpareParts(setSpareParts);
};