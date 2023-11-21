import { useNavigate} from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { getOccurrenceRecordById, sendOccurrenceRecord, getUserById, getProfessionalByCRM } from '../../common/api';
import GenericForm from "./GenericForm";
import { useEffect, useState } from 'react';

export default function OccurrenceForm(){
    const navigate = useNavigate();
    const { patient_id } = useParams();
    const [ healthId, setHealthId] = useState(null)

    const d = new Date()
    async function submitForm(formData){
        let data = {
            "was_emergency" : formData.was_emergency,
            "datetime" : d.getFullYear().toString() +'-' +(d.getMonth() + 1).toString() +'-' +d.getDate().toString() + 'T' + d.getHours().toString() + ':' + d.getMinutes().toString() + ':' + d.getSeconds().toString(),
            "notes" : formData.notes,
            "patient_id": patient_id,
            "healthcare_professional_id": healthId ?? await getProfessionByCRMData(formData.healthcare_professional_id),
        }
        try{
            console.log(data)
            const response = await sendOccurrenceRecord(data)
            console.log(response)
            alert('Registro Criado com Sucesso!')
            navigate('/occurrences')
        }catch(err){
            console.log('deerr')
        }
    }

    useEffect(() => {
        getHealthCareId()
    }, [])

    async function getHealthCareId(){
        if(Number(localStorage.getItem('user_role')) == 2){
            const { data } = await getUserById(localStorage.getItem('user_id'))
            setHealthId(data.healthcare_professional_id)
        }
    }

    async function getProfessionByCRMData(crm){
        const { data } = await getProfessionalByCRM(crm)
        console.log(data)
        setHealthId(data[0].id)
    }

    return(
        <GenericForm 
            title='Ocorrência'
            initialValues={{
                was_emergency: '',
                datetime: new Date(),
                healthcare_professional_id: '',
                patient_id: patient_id,
                notes: ''
            }}
            fieldConfig={{
                was_emergency: { type: 'checkbox' },
                datetime: { type: 'datetime-local'},
                healthcare_professional_id: { type: 'text' },
                patient_id: {type: 'text'},
                notes: {type: 'textarea'}
            }}
            onSubmit={submitForm}
            onLoad={getOccurrenceRecordById}
        />
    )
    
}