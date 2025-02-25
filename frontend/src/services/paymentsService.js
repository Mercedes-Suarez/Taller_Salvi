const API_URL = "http://127.0.0.1:5000/api/payments";

export const getPayments = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getPaymentById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};

export const createPayment = async (paymentData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(paymentData),
    });
    return response.json();
};

export const deletePayment = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};