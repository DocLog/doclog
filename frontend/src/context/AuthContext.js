import React, {createContext} from 'react';
import useAuth from './hooks/useAuth';
const Context = createContext();

function AuthProvider({ children }){
    const {isLogged , handleLogin, error, handleLogout, isLoading} = useAuth()
    
    if(isLoading){
        return (<h1>Loading...</h1>)
    }


    return(
        <Context.Provider value={{ isLogged , handleLogin, error, handleLogout}}> 
            {children}
        </Context.Provider>
    )
}

export { Context , AuthProvider}