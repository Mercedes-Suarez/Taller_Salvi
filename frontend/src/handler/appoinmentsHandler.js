import {
    getAppoinments,
    getAppoinmentById,
    createAppoinment,
    updateAppoinment,
    deleteAppoinment
} from "../services/appoinmentsService";

export const fetchAppoinments = async (setAppoinments) => {
    const data = await getAppoinments();
    setAppoinments(data);
};

export const fetchAppoinmentById = async (id, setAppoinment) => {
    const data = await getAppoinmentById(id);
    setAppoinment(data);
};

export const addAppoinment = async (AppoinmentData, setAppoinment) => {
    await createAppoinment(AppoinmentData);
    fetchAppoinments(setAppoinment);
};

export const editAppoinment = async (id, AppoinmentData, setAppoinment) => {
    await updateAppoinment(id, AppoinmentData);
    fetchAppoinments(setAppoinment);
};

export const removeAppoinment = async (id, setAppoinment) => {
    await deleteAppoinment(id);
    fetchAppoinments(setAppoinment);
};