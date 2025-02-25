import {
    getsession_tokens,
    createsession_tokens,
    updatesession_tokens,
    deletesession_tokens
} from "../services/session_tokensHandler";

export const fetchsession_tokens = async (setsession_tokens) => {
    const data = await getsession_tokens();
    setsession_tokens(data);
};

export const addsession_tokens = async (session_tokensData, setsession_tokens) => {
    await createsession_tokens(session_tokensData);
    fetchsession_tokens(setsession_tokens);
};

export const editsession_tokens = async (id, session_tokensData, setsession_tokens) => {
    await updatesession_tokens(id, session_tokensData);
    fetchsession_tokens(setsession_tokens);
};

export const removesession_tokens = async (id, setsession_tokens) => {
    await deletesession_tokens(id);
    fetchsession_tokens(setsession_tokens);
};