import {
    getRepair_orders,
    getRepair_ordersById,
    createRepair_orders,
    deleteRepair_orders
} from "../services/repair_orderssService";

export const fetchRepair_orders = async (setRepair_orders) => {
    const data = await getRepair_orders();
    setRepair_orders(data);
};

export const fetchRepair_ordersById = async (id, setRepair_orders) => {
    const data = await getRepair_ordersById(id);
    setRepair_orders(data);
};

export const addRepair_orders = async (Repair_ordersData, setRepair_orders) => {
    await createRepair_orders(Repair_ordersData);
    fetchRepair_orders(setRepair_orders);
};

export const removeRepair_orders = async (id, setRepair_orders) => {
    await deleteRepair_orders(id);
    fetchRepair_orders(setRepair_orders);
};