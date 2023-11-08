import React, { useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { Context } from '../context/AuthContext';
import styles from '../styles/Dashboard.module.css'

export default function Dashboard(){
    const {handleLogout, isLogged} = useContext(Context)
    const navigate = useNavigate();

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }
    }, [isLogged, navigate])

    function handleFormMedicine(){
        navigate('/medicines')
    }

    function handleFormCondition(){
        navigate('/conditions')
    }

    function handleFormPatient(){
        navigate('/patients')
    }

    function handleProfile(){
        navigate('/profile')
    }



    return(
        <div className={styles.main}>
            <div className={styles.management_actions}>
                <button onClick={handleProfile}>Configurações de Perfil</button>
                <button onClick={handleLogout}>Sair</button>
            </div>
            
            <div className={styles.container}>
                <h2>Plataforma de Gerenciamento</h2>
                <h3>Escolha uma das opções:</h3>
                <div className={styles.box_2}>
                    <div className={styles.actions}>
                        <button className={styles.action} onClick={handleFormPatient}>Paciente</button>
                        <button className={styles.action} onClick={handleFormCondition}>Condição</button>
                        <button className={styles.action} onClick={handleFormMedicine}>Medicamentos</button>
                    </div>
                </div>
                
            </div>
        </div>
    )
}