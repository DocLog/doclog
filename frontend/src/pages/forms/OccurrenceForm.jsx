import { useNavigate} from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { getOccurrenceRecordById, sendOccurrenceRecord, getUserById, getProfessionalByCRM } from '../../common/api';
import GenericForm from "./GenericForm";
import { useEffect, useState } from 'react';
import { showAlert } from "../../common/swalAlert";

export default function OccurrenceForm(){
    const navigate = useNavigate();
    const { id } = useParams();
    const [ healthId, setHealthId] = useState(null)

    const d = new Date()
    async function submitForm(formData){
        if(!healthId){
            await getProfessionByCRMData(formData.healthcare_professional_id)
        }
        let data = {
            "was_emergency" : formData.was_emergency,
            "datetime" : d.getFullYear().toString() +'-' +(d.getMonth() + 1).toString() +'-' +d.getDate().toString() + 'T' + d.getHours().toString() + ':' + d.getMinutes().toString() + ':' + d.getSeconds().toString(),
            "notes" : formData.notes,
            "patient_id": formData.patient_id,
            "healthcare_professional_id": healthId,
        }
        try{

            await sendOccurrenceRecord(data)
            showAlert('Registro Criado com Sucesso!', 'success')
            navigate('/occurrences/' + formData.patient_id)

        }catch(err){
            if(err.response.status == 422){
                showAlert('Erro ao Salvar os dados!', 'error')
            }

            if(err.response.status == 401){
                showAlert('Não logado! Faça Login', 'error')
            }
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
        setHealthId(data[0].id)
    }

    return(
        <GenericForm 
            title='Ocorrência'
            initialValues={{
                was_emergency: '',
                datetime: new Date(),
                healthcare_professional_id: '',
                patient_id: id,
                notes: ''
            }}
            fieldConfig={{
                was_emergency: { type: 'checkbox' , label: 'É uma emergência?'},
                datetime: { type: 'datetime-local', label: 'Data da Ocorrência'},
                healthcare_professional_id: { type: 'text' , label: 'Id do Profissional'},
                patient_id: {type: 'text', label: 'Id do Paciente'},
                notes: {type: 'textarea', label: 'Observações'}
            }}
            onSubmit={submitForm}
            onLoad={getOccurrenceRecordById}
        />
    )
    
}