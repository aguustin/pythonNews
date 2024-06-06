import { createContext, useState } from "react";
import { uploadNewRequest } from "../api/newsRequests";

const NewContext = createContext()

export const NewContextProvider = ({children}) => {

    const [news, setNews] = useState();

    const uploadNewContext = async (formData) => {
        const res = await uploadNewRequest(formData)
        //setNews([...news, res.data])
    }

    console.log("news: ", news)

    return(
        <NewContext.Provider value={{uploadNewContext}}>{children}</NewContext.Provider>
    )
}

export default NewContext