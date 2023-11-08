import { useNavigate} from 'react-router-dom';
import { getPatientRecordById, sendPatientRecord } from '../../common/api';
import GenericForm from "./GenericForm";

export default function PatientForm( { onFinished } ){
    const navigate = useNavigate();
    const d = new Date()
    async function submitForm(formData){
        let data = {
            "name" : formData.name,
            "surname" : formData.surname,
            "cpf" : formData.cpf,
            "birth_date": formData.birth_date,
            "blood_type": formData.blood_type,
            "register_date": d.getFullYear().toString() +'-' +(d.getMonth() + 1).toString() +'-' +d.getDate().toString() + 'T' + d.getHours().toString() + ':' + d.getMinutes().toString() + ':' + d.getSeconds().toString(),
            "notes": formData.notes
        }
        try{
            console.log(data)
            const response = await sendPatientRecord(data)
            console.log(response)
            onFinished(response)
            alert('Registro Criado com Sucesso!')
        }catch(err){
            console.log('deerr')
        }
    }

    return(
        <GenericForm 
            title='Paciente'
            initialValues={{
                name: '',
                surname: '',
                cpf: '',
                birth_date: Date(),
                blood_type: '',
                notes: ''
            }}
            fieldConfig={{
                name : { type: 'text' },
                surname : { type: 'text'},
                cpf :{ type: 'text'},
                birth_date : {type: 'date'},
                blood_type : {type: 'select', options: ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']},
                notes : {type: 'text'}
            }}
            onSubmit={submitForm}
            onLoad={getPatientRecordById}
        />
    )
    
}