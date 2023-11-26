import { useNavigate} from 'react-router-dom';
import { useParams } from 'react-router-dom';
import { getPatientMedicineRecordById, sendPatientMedicineRecord, updatePatientMedicineRecord} from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

export default function PatientMedicineForm(){
    const navigate = useNavigate();
    const { id, patient_id } = useParams();

    async function submitForm(formData){
        let data = {
            "patient_id": patient_id,
            "medicine_id": formData.medicine_id,
            "notes" : formData.notes,
        }
        try{
            if(id){
                await updatePatientMedicineRecord(id, data)
            }else{
                await sendPatientMedicineRecord(data)
            }
            showAlert('Registro Criado com Sucesso!', 'success')
            navigate('/patient-medicine/' + patient_id)
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
                patient_id: patient_id,
                notes: ''
            }}
            fieldConfig={{
                medicine_id: { type: 'text', label: 'Id do Medicamento', disabled: false},
                patient_id: {type: 'text', label: 'Id do Paciente', disabled: true},
                notes: {type: 'textarea', label: 'Notas', disabled: false}
            }}
            onSubmit={submitForm}
            onLoad={getPatientMedicineRecordById}
        />
    )
    
}