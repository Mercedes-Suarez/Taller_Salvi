import {
    getInvoices,
    getInvoiceById,
    createInvoice,
    deleteInvoice
} from "../services/invoicesService";

export const fetchInvoices = async (setInvoices) => {
    const data = await getInvoices();
    setInvoices(data);
};

export const fetchInvoiceById = async (id, setInvoice) => {
    const data = await getInvoiceById(id);
    setInvoice(data);
};

export const addInvoice = async (invoiceData, setInvoices) => {
    await createInvoice(invoiceData);
    fetchInvoices(setInvoices);
};

export const removeInvoice = async (id, setInvoices) => {
    await deleteInvoice(id);
    fetchInvoices(setInvoices);
};