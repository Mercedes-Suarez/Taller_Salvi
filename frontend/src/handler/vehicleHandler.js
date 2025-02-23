import {
    getVehicles,
    getVehicleById,
    createVehicle,
    updateVehicle,
    deleteVehicle
} from "../services/vehicleService";

export const fetchVehicles = async (setVehicles) => {
    const data = await getVehicles();
    setVehicles(data);
};

export const fetchVehicleById = async (id, setVehicle) => {
    const data = await getVehicleById(id);
    setVehicle(data);
};

export const addVehicle = async (vehicleData, setVehicles) => {
    await createVehicle(vehicleData);
    fetchVehicles(setVehicles);
};

export const modifyVehicle = async (id, vehicleData, setVehicles) => {
    await updateVehicle(id, vehicleData);
    fetchVehicles(setVehicles);
};

export const removeVehicle = async (id, setVehicles) => {
    await deleteVehicle(id);
    fetchVehicles(setVehicles);
};