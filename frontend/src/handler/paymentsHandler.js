import {
    getPayments,
    getPaymentById,
    createPayment,
    deletePayment
} from "../services/paymentsService";

export const fetchPayments = async (setPayments) => {
    const data = await getPayments();
    setPayments(data);
};

export const fetchPaymentById = async (id, setPayment) => {
    const data = await getPaymentById(id);
    setPayment(data);
};

export const addPayment = async (paymentData, setPayments) => {
    await createPayment(paymentData);
    fetchPayments(setPayments);
};

export const removePayment = async (id, setPayments) => {
    await deletePayment(id);
    fetchPayments(setPayments);
};