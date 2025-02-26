import {
    getSpareParts,
    createSparePart,
    updateSparePart,
    deleteSparePart
} from "../services/sparePartsInventoryService";
export const fetchSpareParts = async (setSpareParts) => {
    const data = await getSpareParts();
    if (data.error) {
        console.error("Error fetching spare parts:", data.error);
        return;
    }
    setSpareParts(data);
};

export const addSparePart = async (sparePartData, setSpareParts) => {
    const response = await createSparePart(sparePartData);
    if (response.error) {
        console.error("Error adding spare part:", response.error);
        return;
    }
    fetchSpareParts(setSpareParts);
};

export const editSparePart = async (id, sparePartData, setSpareParts) => {
    const response = await updateSparePart(id, sparePartData);
    if (response.error) {
        console.error("Error updating spare part:", response.error);
        return;
    }
    fetchSpareParts(setSpareParts);
};

export const removeSparePart = async (id, setSpareParts) => {
    const response = await deleteSparePart(id);
    if (response.error) {
        console.error("Error deleting spare part:", response.error);
        return;
    }
    fetchSpareParts(setSpareParts);
};