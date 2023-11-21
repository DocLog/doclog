import { useState, useContext, useEffect } from "react";
import { Context } from "../../context/AuthContext";
import { useNavigate, useParams } from 'react-router-dom';
import styles from '../../styles/Form.module.css'

export default function GenericForm({ title, initialValues, fieldConfig, onSubmit, onLoad}){
    const { isLogged } = useContext(Context);
    const navigate = useNavigate();
    const { id } = useParams();

    const [formData, setFormData] = useState(initialValues ?? {})

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }

        if(id){
            onLoad(id).then(({data}) =>{
                console.log(data)
                Object.keys(data).map((obj) => {
                    
                    setFormData(formData => ({ ...formData, [obj] : data[obj]}))
                    
                    return true;
                })
            })
            
        }
    }, [isLogged, navigate, id, onLoad])

    function submitForm(){
        onSubmit(formData);
    }

    function handleFieldChange(fieldName, value){
        setFormData({...formData, [fieldName] : value})
    }
    
    function renderFields(fieldName, fieldData){
        const { type, options} = fieldData
        if(type === 'textarea'){
            return(<textarea
                        type="text"
                        placeholder={fieldName}
                        id={fieldName}
                        name={fieldName}
                        value={formData[fieldName]}
                        rows='3'
                        onChange={(e) => handleFieldChange(fieldName, e.target.value)}
                        />)
        }else if(type === 'select'){
            return(
                <select name={fieldName} onChange={(e) => handleFieldChange(fieldName, e.target.value)} value={formData[fieldName]}>
                    <option value="">Selecione uma opção</option>
                    {options.map((opt) => {
                        return <option key={opt} value={opt}>{opt}</option>
                        
                    }) }
                </select>
            )
        }else if(type === 'checkbox'){
            return(
                <input
                type={type}
                placeholder={fieldName}
                id={fieldName}
                name={fieldName}
                value={formData[fieldName]}
                onChange={(e) => handleFieldChange(fieldName, e.target.checked)}
            />
            )
        }else{
            return(
                <input
                    type={type}
                    placeholder={fieldName}
                    id={fieldName}
                    name={fieldName}
                    value={formData[fieldName]}
                    onChange={(e) => handleFieldChange(fieldName, e.target.value)}
                />
            )
        }

       
    }

    return(
        <div className={styles.form}>
        <h2>{title}</h2>
        <div className={styles.form_fields}>
            {Object.keys(formData).map((field) => (
                field !== 'id' ?
                <div key={field} className={styles.form_group}>
                    <label htmlFor={field}>{field.charAt(0).toUpperCase() + field.slice(1)}</label>
                    {field !== 'id' ? renderFields(field, fieldConfig[field]) : ''}
                </div> 
                : ''
            ))}
            
            
            </div>
            <div className={styles.button_container}>
                <button onClick={submitForm}>Salvar</button>
            </div>
        
    </div>
    )
}