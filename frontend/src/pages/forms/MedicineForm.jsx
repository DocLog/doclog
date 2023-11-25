import { useNavigate, useParams } from 'react-router-dom';
import { getMedicineRecordById, sendMedicineRecord , updateMedicineRecord} from '../../common/api';
import GenericForm from "./GenericForm";
import { showAlert } from "../../common/swalAlert";

export default function MedicineForm(){
    const navigate = useNavigate();
    const { id } = useParams();
    
    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "description" : formData.description,
            "dosage" : Number(formData.dosage),
            "dosage_unit": formData.dosage_unit
        }

        try{

            if(id){
                await updateMedicineRecord(id, data)
            }else{
                await sendMedicineRecord(data)
            }
            
            showAlert('Registro Criado com Sucesso!', 'success')
            navigate('/medicines')

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
            title='Medicamento'
            initialValues={{
                name: '',
                dosage: 0,
                dosage_unit: '',
                description: ''
            }}
            fieldConfig={{
                name : { type: 'text' , label: 'Nome do medicamento'},
                dosage : { type: 'number', label: 'Dosagem'},
                dosage_unit : {type: 'select', options: ['mg', 'ml'], label: 'Unidade da Dosagem'},
                description : {type: 'textarea', label: 'Descrição'}
            }}
            onSubmit={submitForm}
            onLoad={getMedicineRecordById}
        />
    )
    
}