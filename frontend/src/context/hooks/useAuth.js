import { useState, useEffect } from "react";
import { sendLoginData } from '../../common/api';

export default function useAuth(){
    const [ isLogged, setIsLogged] = useState(false)
    const [ isLoading, setLoading] = useState(true);
    const [ error, setError] = useState('');

    useEffect(() => {
        const token = localStorage.getItem('token')

        if(token){
            setIsLogged(true)
        }
        setLoading(false)
    }, [])

    async function handleLogin(username, password){
        // setIsLogged(true);
        try{
            const {data} = await sendLoginData(username, password)
            console.log(data)
            if(data){
                setIsLogged(true);
                localStorage.setItem('token', JSON.stringify(data.access_token))
                localStorage.setItem('user_role', JSON.stringify(data.user_role))
                localStorage.setItem('user_id', JSON.stringify(data.user_id))
                
            }
        }catch(e){
            setIsLogged(false)
            setError('Credenciais inválidas')
        }
        
        
        setLoading(false);
    }

    function handleLogout(){
        setIsLogged(false);
        localStorage.clear()
    }

    return {isLogged , handleLogin, error, handleLogout, isLoading}
}