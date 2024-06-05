import { createContext, useEffect, useState } from "react";
import { getInRequest } from '../api/userRequests';
import { useNavigate } from "react-router-dom";

 const UserContext = createContext();

export const UserContextProvider = ({children}) => {
    const [session, setSession] = useState(null)
    const navigate = useNavigate()

    useEffect(() => {
        setSession(JSON.parse(localStorage.getItem('user')))
    }, [])
    console.log(session)
    const getInContext = async (data) => {
        const res = await getInRequest(data);
        localStorage.removeItem('user')
        localStorage.setItem('user', JSON.stringify(res.data[0]))
        setSession(JSON.parse(localStorage.getItem('user')))

        if(res.data.length > 0){
            navigate('/home')
        }else{
            alert("Las credenciales ingresadas son incorrectas")
        }
    }

    return(
        <UserContext.Provider value={{session, setSession, getInContext}}>{children}</UserContext.Provider>
    )
}

export default UserContext;