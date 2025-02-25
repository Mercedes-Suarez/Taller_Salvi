const API_URL = "http://127.0.0.1:5000/api/invoices";

export const getInvoices = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getInvoiceById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};

export const createInvoice = async (invoiceData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(invoiceData),
    });
    return response.json();
};

export const deleteInvoice = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};
