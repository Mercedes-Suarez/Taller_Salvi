import {
    getchat_Messages,
    getchat_MessageById,
    createchat_Message,
    updatechat_Message,
    deletechat_Message
} from "../services/chat_messagesService";

export const fetchchat_Messages = async (setchat_Messages) => {
    const data = await getchat_Messages();
    setchat_Messages(data);
};

export const fetchchat_MessageById = async (id, setchat_Message) => {
    const data = await getchat_MessageById(id);
    setchat_Message(data);
};

export const addchat_chat_Message = async (chat_messageData, setchat_Message) => {
    await createchat_Message(chat_messageData);
    fetchchat_Messages(setchat_Message);
};

export const editchat_Message = async (id, chat_messageData, setChat_Messages) => {
    await updatechat_Message(id, chat_messageData);
    fetchchat_Messages(setchat_Messages);
};

export const removeMessage = async (id, setchat_Messages) => {
    await deletechat_Message(id);
    fetchchat_Messages(setchat_Messages);
};