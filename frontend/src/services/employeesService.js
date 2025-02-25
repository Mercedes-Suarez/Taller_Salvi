const API_URL = "http://127.0.0.1:5000/api/employees";

export const getEmployee = async () => {
    const response = await fetch(API_URL);
    return response.json();
};

export const getEmployeeById = async (id) => {
    const response = await fetch(`${API_URL}/${id}`);
    return response.json();
};

export const createEmployee = async (EmployeeData) => {
    const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(EmployeeData),
    });
    return response.json();
};

export const deleteEmployee = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
};