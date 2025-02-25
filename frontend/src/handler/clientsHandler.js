import {
    getClients,
    createClients,
    updateClients,
    deleteClients
} from "../services/clientsServices";

export const fetchClients = async (setClients) => {
    const data = await getClients();
    setClients(data);
};

export const addClients = async (ClientsData, setClients) => {
    await createClients(ClientsData);
    fetchClients(setClients);
};

export const editClients = async (id, ClientsData, setClients) => {
    await updateClients(id, ClientsData);
    fetchClients(setClients);
};

export const removeClients = async (id, setClients) => {
    await deleteClients(id);
    fetchClients(setClients);
};