import React, { useEffect, useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { Context } from '../context/AuthContext';
import styles from '../styles/Login.module.css'

export default function Login() {
    const { isLogged, handleLogin , error} = useContext(Context);

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        if(isLogged){
            navigate('/dashboard')
        }
    }, [isLogged, navigate])

    async function submitForm(){
        await handleLogin(username, password)
    }

    
    return (
        <div className={styles.main}>
            <div className={styles.form}>
            <h2>Login</h2>
                <div className={styles.form_group}>
                    <input
                        type="text"
                        placeholder="Username"
                        id="username"
                        name="username"
                        className={styles.field}
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div className={styles.form_group}>
                    <input
                        type="password"
                        placeholder="password"
                        id="password"
                        name="password"
                        className={styles.field}
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        />
                </div>
                <div>{error}</div>
                <div className={styles.button_container}>
                    <button onClick={submitForm}>Login</button>
                </div>
            </div>
        </div>
    );
}