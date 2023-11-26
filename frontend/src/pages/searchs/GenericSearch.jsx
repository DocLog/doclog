
import { useContext, useEffect, useState } from 'react'
import styles from '../../styles/Search.module.css'

import { Context } from '../../context/AuthContext'
import { useNavigate, useParams } from 'react-router-dom'
import Card from '../../components/Card'

export default function GenericSearch({ placeholder, path, getRecords, getRecordsFromPatient, deleteRecord, isDeleted, isChanged}){

    const { isLogged } = useContext(Context)
    const [properties, setProperties] = useState([])
    const [search, setSearch] = useState([])
    const [textSearch, setTextSearch] = useState('')
    const navigate = useNavigate()
    const { patient_id } = useParams()

    useEffect(() => {
        handleGetRecords()
    }, [])

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }
    }, [isLogged, properties, navigate, search])

    async function handleGetRecords(){
        if(patient_id){
            const { data } = await getRecordsFromPatient(patient_id);

            setProperties(data);
            setSearch(data);
        }else{
            const { data } = await getRecords();

            setProperties(data);
            setSearch(data);
        }
        
    }

    function onSearch(){
        const data = properties.filter((obj) => (
            obj.name?.toUpperCase().includes(textSearch.toUpperCase()) || 
            obj.id?.toString().toUpperCase().includes(textSearch.toUpperCase()) || 
            obj.cpf?.toUpperCase().includes(textSearch.toUpperCase()))
        )

        setSearch(data)
    }


    function addAction(e){
        if(patient_id){
            navigate(path + patient_id)
        }else{
            navigate(path)
        }

    }

    function editAction(e){
        if(patient_id){
            navigate(path +  patient_id + '/' + e.target.id)
        }else{
            navigate(path+ e.target.id)
        }
    }

    function deleteAction(e){
        deleteRecord(e.target.id).then((response) => {
            handleGetRecords();
        })
    }

    return(
        <div className={styles.container_medicine}>
            <div id='search-area' className={styles.group}>
                <input name='search' placeholder={placeholder} className={styles.input_medicine} onChange={(e) => {setTextSearch(e.target.value)}}></input>
                <button className={styles.button_search} onClick={onSearch}>Pesquisar</button>
                <button className={styles.button_search} id={patient_id} onClick={addAction}>Adicionar</button>
            </div>
            <div id='results' className={styles.box_medicine}>
                { search.map(function(e) {
                    console.log(e)
                    return(<Card key={e.id} id={e.id} content={(e.name ?? (e.id))} isDeleted={isDeleted} isChanged={isChanged} onEdit={editAction} onDelete={deleteAction}/>)
                })}
            </div>
        </div>
    )
}