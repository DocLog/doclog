
import { useContext, useEffect, useState } from 'react'
import styles from '../../styles/Search.module.css'

import { Context } from '../../context/AuthContext'
import { useNavigate, useParams } from 'react-router-dom'
import Card from '../../components/Card'

export default function GenericSearch({ placeholder, path, getRecords, getRecordsFromPatient, deleteRecord, isDeleted, isChanged}){

    const { isLogged } = useContext(Context)
    const [properties, setProperties] = useState([])
    const navigate = useNavigate()
    const { id } = useParams()

    useEffect(() => {
        handleGetRecords()
    }, [])

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }
    }, [isLogged, properties, navigate])

    async function handleGetRecords(){
        console.log(id)
        if(id){
            const { data } = await getRecordsFromPatient(id);

            setProperties(data);
        }else{
            const { data } = await getRecords();

            setProperties(data);
        }
        
    }

    function addAction(e){
        navigate(path+ e.target.id)
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
                <button className={styles.button_search} id={id} onClick={addAction}>Adicionar</button>
            </div>
            <div id='results' className={styles.box_medicine}>
                { properties.map(function(e) {
                    console.log(e)
                    return(<Card key={e.id} id={e.id} content={(e.name ?? ('Occorência ' + e.id))} isDeleted={isDeleted} isChanged={isChanged} onEdit={editAction} onDelete={deleteAction}/>)
                })}
            </div>
        </div>
    )
}