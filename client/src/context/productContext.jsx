import { createContext, useState } from "react";
import { uploadNewRequest } from "../api/newsRequests";

const NewContext = createContext()

export const NewContextProvider = ({children}) => {

    const [news, setNews] = useState();

    const uploadNewContext = async (userId, formData, categories) => {
        const res = uploadNewRequest(userId, formData, categories)
        //setNews([...news, res.data])
    }

    console.log("news: ", news)

    return(
        <NewContext.Provider value={{uploadNewContext}}>{children}</NewContext.Provider>
    )
}

export default NewContext