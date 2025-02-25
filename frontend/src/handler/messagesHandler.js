import {
    getMessages,
    createMessage,
    updateMessage,
    deleteMessage
} from "../services/messagesService";

export const fetchMessages = async (setMessages) => {
    const data = await getMessages();
    setMessages(data);
};

export const addMessage = async (messageData, setMessages) => {
    await createMessage(messageData);
    fetchMessages(setMessages);
};

export const editMessage = async (id, messageData, setMessages) => {
    await updateMessage(id, messageData);
    fetchMessages(setMessages);
};

export const removeMessage = async (id, setMessages) => {
    await deleteMessage(id);
    fetchMessages(setMessages);
};