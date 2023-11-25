import { useState, useContext, useEffect } from "react";
import { Context } from "../../context/AuthContext";
import { useNavigate, useParams } from 'react-router-dom';
import styles from '../../styles/Form.module.css';
import { isEmptyFields, isValidDate } from '../../common/validation';
import Swal from "sweetalert2";

export default function GenericForm({ title, initialValues, fieldConfig, onSubmit, onLoad}){
    const { isLogged } = useContext(Context);
    const navigate = useNavigate();
    const { id } = useParams();

    const [formData, setFormData] = useState(initialValues ?? {})

    function showAlert(message){
        Swal.fire({
            title: "Mensagem",
            text: message,
            icon: "info",
            confirmButtonText: 'OK'
        })
    }

    useEffect(() => {
        if(!isLogged){
            navigate('/login')
        }

        if(id){
            onLoad(id).then(({data}) =>{
                console.log(data)
                Object.keys(data).map((obj) => {
                    
                    setFormData(formData => ({ ...formData, [obj] : data[obj]}))
                    
                    console.log(formData)
                    return true;
                })
            })
            
        }
    }, [isLogged, navigate, id, onLoad])

    function submitForm(){
        let result1 = isEmptyFields(formData);
        let result2 = isValidDate(formData);
        if(result1.length !== 0){
            showAlert(result1)
            return;
        }
        if(result2.length !== 0){
            showAlert(result2)
            return;
        }
        onSubmit(formData);
    }

    function handleFieldChange(fieldName, value){
        setFormData({...formData, [fieldName] : value})
    }
    
    function renderFields(fieldName, fieldData){
        const { type, options, label} = fieldData
        if(type === 'textarea'){
            return(
            <>
                <label htmlFor={fieldName}>{label.charAt(0).toUpperCase() + label.slice(1)}</label>
                <textarea
                    type="text"
                    placeholder={label}
                    id={fieldName}
                    name={fieldName}
                    value={formData[fieldName]}
                    rows='3'
                    onChange={(e) => handleFieldChange(fieldName, e.target.value)}
                />
            </>
            )
        }else if(type === 'select'){
            return(
                <>
                    <label htmlFor={fieldName}>{label.charAt(0).toUpperCase() + label.slice(1)}</label>
                    <select name={fieldName} onChange={(e) => handleFieldChange(fieldName, e.target.value)} value={formData[fieldName]}>
                        <option value="">Selecione uma opção</option>
                        {options.map((opt) => {
                            return <option key={opt} value={opt}>{opt}</option>
                            
                        }) }
                    </select>
                </>
                
            )
        }else if(type === 'checkbox'){
            return(
                <>
                    <label htmlFor={fieldName}>{label.charAt(0).toUpperCase() + label.slice(1)}</label>
                    <input
                    type={type}
                    placeholder={label}
                    id={fieldName}
                    name={fieldName}
                    value={formData[fieldName]}
                    onChange={(e) => handleFieldChange(fieldName, e.target.checked)}
                    />
                </>
                
            )
        }else{
            return(
                <>
                    <label htmlFor={fieldName}>{label.charAt(0).toUpperCase() + label.slice(1)}</label>
                    <input
                        type={type}
                        placeholder={label}
                        id={fieldName}
                        name={fieldName}
                        value={formData[fieldName]}
                        onChange={(e) => handleFieldChange(fieldName, e.target.value)}
                    />
                </>
                
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