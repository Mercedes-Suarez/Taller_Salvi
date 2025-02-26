import {
    getsessionTokens,
    createsessionTokens,
    updatesessionTokens,
    deletesessionTokens
} from "../services/session_tokensService";
export const fetchSessionTokens = async (setSessionTokens) => {
    try {
        const data = await getSessionTokens();
        setSessionTokens(data);
    } catch (error) {
        console.error("Error fetching session tokens:", error);
    }
};

export const addSessionToken = async (sessionTokenData, setSessionTokens) => {
    try {
        await createSessionToken(sessionTokenData);
        fetchSessionTokens(setSessionTokens);
    } catch (error) {
        console.error("Error adding session token:", error);
    }
};

export const editSessionToken = async (id, sessionTokenData, setSessionTokens) => {
    try {
        await updateSessionToken(id, sessionTokenData);
        fetchSessionTokens(setSessionTokens);
    } catch (error) {
        console.error("Error updating session token:", error);
    }
};

export const removeSessionToken = async (id, setSessionTokens) => {
    try {
        await deleteSessionToken(id);
        fetchSessionTokens(setSessionTokens);
    } catch (error) {
        console.error("Error deleting session token:", error);
    }
};