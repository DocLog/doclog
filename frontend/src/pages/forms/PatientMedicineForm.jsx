import { useNavigate} from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { getPatientMedicineRecordById, sendPatientMedicineRecord} from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

export default function PatientMedicineForm(){
    const navigate = useNavigate();
    const { id } = useParams();

    async function submitForm(formData){
        let data = {
            "patient_id": id ?? formData.patient_id,
            "medicine_id": formData.medicine_id,
            "notes" : formData.notes,
        }
        try{
            await sendPatientMedicineRecord(data)
            showAlert('Registro Criado com Sucesso!', 'success')
            navigate('/patient-medicine/' + formData.patient_id)
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
            title='Medicamentos relacionado ao paciente'
            initialValues={{
                medicine_id: '',
                patient_id: id ?? '',
                notes: ''
            }}
            fieldConfig={{
                medicine_id: { type: 'text', label: 'Id do Medicamento'},
                patient_id: {type: 'text', label: 'Id do Paciente'},
                notes: {type: 'textarea', label: 'Notas'}
            }}
            onSubmit={submitForm}
            onLoad={getPatientMedicineRecordById}
        />
    )
    
}