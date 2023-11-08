

import { useContext, useEffect, useState} from 'react'
import { useNavigate } from 'react-router-dom'
import { getUserById } from '../common/api'
import { Context } from '../context/AuthContext'
import styles from '../styles/Profile.module.css'

export default function Profile(){
    const { isLogged } = useContext(Context)
    const [ user, setUser] = useState({})
    const navigate = useNavigate()
    

    useEffect(() => {
        handleGetUser()
    }, [])

    async function handleGetUser(){
        const { data } = await getUserById(JSON.parse(localStorage.getItem('user_id'))) 
        console.log(data)
        setUser(data)
        
        
    }

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }
    }, [isLogged, navigate])


    function handleManagement(){
        navigate('/form-user/')
    }

    return(
       <div className={styles.container}>
        <h2>Configurações de Perfil</h2>
        <fieldset className={styles.container_information}>
            <legend>Informações sobre o usuário</legend>
            <div>
                <section><strong>Id:</strong></section>
                <section>{user.id}</section>
            </div>
            <div>
                <section><strong>Nome:</strong></section>
                <section>{user.name}</section>
            </div>
            <div>
                <section><strong>Email:</strong></section>
                <section>{user.email}</section>
            </div>
        </fieldset>
        <fieldset>
            <legend>Ações</legend>
            <div className={styles.actions}>
                <button className={styles.action}>Alterar Informações</button>
                <button className={styles.action} onClick={handleManagement}>Gerenciar Usuários</button>
            </div>
        </fieldset>
       </div>
    )
}