import {
    getRepair_details,
    getRepair_detailsById,
    createRepair_details,
    deleteRepair_details
} from "../services/repair_detailsService";

export const fetchRepair_details = async (setRepair_details) => {
    const data = await getRepair_details();
    setRepair_details(data);
};

export const fetchRepair_detailsById = async (id, setRepair_details) => {
    const data = await getRepair_detailsById(id);
    setRepair_details(data);
};

export const addRepair_details = async (Repair_detailsData, setRepair_details) => {
    await createRepair_details(Repair_detailsData);
    fetchRepair_details(setRepair_details);
};

export const removeRepair_details = async (id, setRepair_details) => {
    await deleteRepair_details(id);
    fetchRepair_details(setRepair_details);
};
