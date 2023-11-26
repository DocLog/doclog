import { useNavigate} from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { getPatientConditionRecordById, sendPatientConditionRecord, updatePatientConditionRecord } from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

export default function PatientConditionForm(){
    const navigate = useNavigate();
    const { id, patient_id } = useParams();

    async function submitForm(formData){
        let data = {
            "patient_id": patient_id,
            "condition_id": formData.condition_id,
            "notes" : formData.notes,
        }
        try{
            if(id){
                await updatePatientConditionRecord(id, data)
            }else{
                await sendPatientConditionRecord(data)
            }
            showAlert('Registro Criado com Sucesso!', 'success')
            navigate('/patient-condition/' + formData.patient_id)
        }catch(err){
            if(err.response.status == 422){
                showAlert('Erro ao Salvar os dados!', 'error')
            }

            if(err.response.status == 401){
                showAlert('Não logado! Faça Login', 'error')
            }
        }
    }


    return(
        <GenericForm 
            title='Condições relacionadas ao paciente'
            initialValues={{
                condition_id: '',
                patient_id: patient_id,
                notes: ''
            }}
            fieldConfig={{
                condition_id: { type: 'text', label: 'Id da Condição'},
                patient_id: {type: 'text', label: 'Id do Paciente'},
                notes: {type: 'textarea', label: 'Notas'}
            }}
            onSubmit={submitForm}
            onLoad={getPatientConditionRecordById}
        />
    )
    
}