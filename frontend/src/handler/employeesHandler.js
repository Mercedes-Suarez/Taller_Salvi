import {
    getEmployee,
    createEmployee,
    updateEmployee,
    deleteEmployee
} from "../services/EmployeesServices";

export const fetchEmployee = async (setEmployee) => {
    const data = await getEmployee();
    setEmployee(data);
};

export const addEmployee = async (EmployeeData, setEmployee) => {
    await createEmployee(EmployeeData);
    fetchEmployee(setEmployee);
};

export const editEmployee = async (id, EmployeeData, setEmployee) => {
    await updateEmployee(id, EmployeeData);
    fetchEmployee(setEmployee);
};

export const removeEmployee = async (id, setEmployee) => {
    await deleteEmployee(id);
    fetchEmployee(setEmployee);
};