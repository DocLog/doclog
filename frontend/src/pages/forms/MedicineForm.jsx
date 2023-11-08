import { useNavigate} from 'react-router-dom';
import { getMedicineRecordById, sendMedicineRecord } from '../../common/api';
import GenericForm from "./GenericForm";

export default function MedicineForm(){
    const navigate = useNavigate();


    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "description" : formData.description,
            "dosage" : Number(formData.dosage),
            "dosage_unit": formData.dosage_unit
        }
        try{
            console.log(data)
            const response = await sendMedicineRecord(data)
            console.log(response)
            alert('Registro Criado com Sucesso!')
            navigate('/medicines')
        }catch(err){
            console.log('deerr')
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
                name : { type: 'text' },
                dosage : { type: 'number'},
                dosage_unit : {type: 'select', options: ['mg', 'ml']},
                description : {type: 'textarea'}
            }}
            onSubmit={submitForm}
            onLoad={getMedicineRecordById}
        />
    )
    
}