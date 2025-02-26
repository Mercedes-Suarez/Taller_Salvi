import {
    getUserTypes,
    createUserType,
    updateUserType,
    deleteUserType
} from "../services/userTypeService";

export const fetchUserTypes = async (setUserTypes) => {
    const data = await getUserTypes();
    if (data.error) {
        console.error("Error fetching user types:", data.error);
        return;
    }
    setUserTypes(data);
};

export const addUserType = async (userTypeData, setUserTypes) => {
    const response = await createUserType(userTypeData);
    if (response.error) {
        console.error("Error adding user type:", response.error);
        return;
    }
    fetchUserTypes(setUserTypes);
};

export const editUserType = async (id, userTypeData, setUserTypes) => {
    const response = await updateUserType(id, userTypeData);
    if (response.error) {
        console.error("Error updating user type:", response.error);
        return;
    }
    fetchUserTypes(setUserTypes);
};

export const removeUserType = async (id, setUserTypes) => {
    const response = await deleteUserType(id);
    if (response.error) {
        console.error("Error deleting user type:", response.error);
        return;
    }
    fetchUserTypes(setUserTypes);
};