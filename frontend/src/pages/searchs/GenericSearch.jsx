
import { useContext, useEffect, useState } from 'react'
import styles from '../../styles/Search.module.css'

import { Context } from '../../context/AuthContext'
import { useNavigate } from 'react-router-dom'
import Card from '../../components/Card'

export default function GenericSearch({ placeholder, path, getRecords, deleteRecord, isDeleted, isChanged}){

    const { isLogged } = useContext(Context)
    const [properties, setProperties] = useState([])
    const navigate = useNavigate()

    useEffect(() => {
        handleGetRecords()
    }, [])

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }
    }, [isLogged, properties, navigate])

    async function handleGetRecords(){
        const { data } = await getRecords();

        setProperties(data);

    }

    function addAction(e){
        navigate(path)
    }

    function editAction(e){
        navigate(path+ e.target.id)
    }

    function deleteAction(e){
        deleteRecord(e.target.id).then((response) => {
            handleGetRecords();
        })
    }

    return(
        <div className={styles.container_medicine}>
            <div id='search-area' className={styles.group}>
                <input name='search' placeholder={placeholder} className={styles.input_medicine}></input>
                <button className={styles.button_search}>Pesquisar</button>
                <button className={styles.button_search} onClick={addAction}>Adicionar</button>
            </div>
            <div id='results' className={styles.box_medicine}>
                { properties.map(function(e) {
                    return(<Card key={e.id} id={e.id} content={e.name} isDeleted={isDeleted} isChanged={isChanged} onEdit={editAction} onDelete={deleteAction}/>)
                })}
            </div>
        </div>
    )
}